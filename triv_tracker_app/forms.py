from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input d-inline-block w-50 m-0", "placeholder": "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "form-control login-input d-inline-block w-50 m-0", "placeholder": "Password"}))

    class Meta:
        model = models.LoginModel
        fields = ('username', 'password')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Last Name"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Email"}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "form-control login-input", "placeholder": "Password"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
    points = 0

    class Meta:
        model = models.UserProfile
        fields = ()

class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Last Name"}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Username"}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control login-input", "placeholder": "Email", "type": "email"}))

    class Meta:
        model = models.UpdateModel
        fields = ('first_name', 'last_name', 'username', 'email',)

class CodeForm(forms.ModelForm):
    code = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "code-input", "placeholder": "Enter Code"}))

    class Meta:
        model = models.Code
        fields = ('code',)
