from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import datetime

def format_string(string):
    string = string.lower()
    final_string = ""
    for i in string:
        if i == " ":
            final_string += "_"
        elif i not in ["!", ","]:
            final_string += i

    return final_string

def index(request):
    if request.user.is_authenticated:
        profile = models.UserProfile.objects.filter(user=request.user)[0]
        if profile.is_mentor:
            code = models.MentorCode.objects.filter(user=profile)[0].code
        else:
            code = None
        context_dict = {"profile": profile, "code": code}
    else:
        context_dict = {}
    return render(request, "triv_tracker_app/index.html", context=context_dict)

def user_login(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            print(user)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    login_form.add_error("username", "Account now inactive. Please register again.")
            else:
                login_form.add_error("username", "Username or password incorrect. Please try again.")

    else:
        login_form = forms.LoginForm()

    return render(request, "triv_tracker_app/login.html", context={"form": login_form})

def register(request):
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        # profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = models.UserProfile(user=user, points=0)
            profile.save()

            record = models.AchievementRecord(user=user)
            record.save()

            login(request, user)
            return HttpResponseRedirect("/")

    else:
        user_form = forms.UserForm()

    context_dict = {
        "user_form": user_form,
    }

    return render(request, "triv_tracker_app/register.html", context=context_dict)

@login_required(login_url="/login/")
def update(request):
    profile = models.UserProfile.objects.filter(user=request.user)[0]
    if request.method == "POST":
        form = forms.UpdateForm(request.POST)

        if form.is_valid():
            user = User.objects.filter(username=request.user.username)[0]

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            if profile.is_mentor:
                mentor_code = models.MentorCode.objects.filter(user=profile)[0]
                mentor_code.code = request.POST.get('code')
                mentor_code.save()
            user.save()

            messages.success(request, "Account successfully updated!")

        else:
            print(form.errors)

    else:
        form = forms.UpdateForm(initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "username": request.user.username,
            "email": request.user.email,
        })

    if profile.is_mentor:
        context_dict = {
            "form": form,
            "profile": profile,
            "code": models.MentorCode.objects.filter(user=profile)[0].code
        }
    else:
        context_dict = {
            "form": form,
            "profile": profile
        }

    return render(request, "triv_tracker_app/update.html", context=context_dict)

@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url="/login/")
def achievements(request):
    errors = None
    achievements = models.Achievement.objects.all() # Getting all achievements
    categories = list(set([achievement.category for achievement in achievements])) # Picking out unique categories
    categories = {category: [] for category in categories} # Storing it into dictionary with empty lists

    for achievement in achievements: # Appending respective achievements to certain categories
        category = achievement.category
        achievements_category = models.Achievement.objects.filter(category=category)
        full_achievements = []
        for achievement in achievements_category:
            title = achievement.name
            formatted_title = format_string(title)
            record = models.AchievementRecord.objects.filter(user=request.user)[0]
            obj = {}
            try:
                obj[achievement] = getattr(record, formatted_title)
            except:
                obj[achievement] = False

            full_achievements.append(obj)
        categories[category] = [i for i in list(full_achievements)]

    if request.method == "POST":
        form = forms.CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            reward = request.POST.get('reward')
            last_achievement_name = request.POST.get("last_achievement_name")
            last_achievement_time = datetime.datetime.now()
            matching_code = models.MentorCode.objects.filter(code=code)

            if matching_code:
                user = models.UserProfile.objects.filter(user=request.user)[0]
                user.points += int(reward)
                user.last_achievement_name = last_achievement_name
                user.last_achievement_time = last_achievement_time
                user.save()

                record = models.AchievementRecord.objects.filter(user=request.user)[0]
                setattr(record, format_string(last_achievement_name), True)
                record.save()

                return HttpResponseRedirect("/achievements/")

            else:
                form.add_error("code", "Invalid code.")

    else:
        form = forms.CodeForm()

    return render(request, "triv_tracker_app/achievements.html", context={"categories": categories, "form": form, "profile": models.UserProfile.objects.filter(user=request.user)[0]})

@login_required(login_url="/login/")
def progress(request):
    user = models.UserProfile.objects.filter(user=request.user)[0]
    history = user.history.all()

    records = {}

    for record in history:
        name = record.last_achievement_name
        if name == "No achievements yet":
            break
        else:
            achievement = models.Achievement.objects.filter(name=name)[0]
            time = record.last_achievement_time
            if time in records.keys():
                records[time] += [achievement]
            else:
                records[record.last_achievement_time] = [achievement]

    return render(request, "triv_tracker_app/progress.html", context={"records": records})

@login_required(login_url="/login/")
def leaderboards(request):
    users = models.UserProfile.objects.raw("select * from triv_tracker_app_UserProfile order by points desc limit 5")
    leaderboards = {}
    for i in range(len(users)):
        if not users[i].is_mentor:
            leaderboards[i+1] = users[i]

    context_dict = {
        "users": leaderboards,
        "profile": models.UserProfile.objects.filter(user=request.user)[0]
    }

    return render(request, "triv_tracker_app/leaderboards.html", context=context_dict)

@login_required(login_url="/login/")
def leaderboards_all(request):
    users = models.UserProfile.objects.raw("select * from triv_tracker_app_UserProfile order by points desc")
    leaderboards = {}
    for i in range(len(users)):
        if not users[i].is_mentor:
            leaderboards[i+1] = users[i]

    context_dict = {
        "users": leaderboards,
        "profile": models.UserProfile.objects.filter(user=request.user)[0]
    }

    return render(request, "triv_tracker_app/leaderboards_all.html", context=context_dict)

@login_required(login_url="/login/")
def my_account(request):
    return render(request, "triv_tracker_app/my_account.html", context={"profile": models.UserProfile.objects.filter(user=request.user)[0]})

def contact_us(request):
    return render(request, "triv_tracker_app/contact-us.html", context={"profile": models.UserProfile.objects.filter(user=request.user)[0]})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "registration/activate_email_confirmation.html")
    else:
        return render(request, "registration/invalid_link.html")

@login_required(login_url="/login/")
def enter_code(request):
    if request.method == "POST":
        form = forms.CodeForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['code']

            matching_code = models.Code.objects.filter(code=code)

            if matching_code:
                user = models.UserProfile.objects.filter(user=request.user)[0]
                if code == user.last_code:
                    form.add_error("code", "You've already used this code!")
                else:
                    messages.success(request, "Nice! You gained {} points!".format(matching_code[0].amount))
                    user.points = user.points + matching_code[0].amount
                    user.last_code = code
                    user.save()

            else:
                form.add_error("code", "Invalid code.")

    else:
        form = forms.CodeForm()

    return render(request, "triv_tracker_app/enter_code.html", context={"form": form})
