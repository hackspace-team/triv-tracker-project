from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
import uuid

User._meta.get_field('username')._unique = True
User._meta.get_field('email')._unique = True

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    points = models.IntegerField()
    last_achievement_name = models.CharField(max_length=100, default="No achievements yet")
    last_achievement_time = models.DateField(null=True)
    last_code = models.CharField(max_length=100, default="None")
    is_mentor = models.BooleanField(default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=50)
    long_description = models.CharField(max_length=400)
    reward = models.IntegerField()

    def __str__(self):
        return self.name

class AchievementRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # loops_2 = models.BooleanField(default=False)
    # loops_1 = models.BooleanField(default=False)
    # control_flow = models.BooleanField(default=False)
    # pair_up = models.BooleanField(default=False)
    # strings = models.BooleanField(default=False)
    # variables = models.BooleanField(default=False)
    # hello_world = models.BooleanField(default=False)
    # get_installed = models.BooleanField(default=False)
    # lightning_talk = models.BooleanField(default=False)
    # pair_up = models.BooleanField(default=False)
    # html_page = models.BooleanField(default=False)
    # technical_mentor = models.BooleanField(default=False)
    # let_me_teach = models.BooleanField(default=False)
    # attention = models.BooleanField(default=False)
    # hear_ye = models.BooleanField(default=False)
    # complete_1_level = models.BooleanField(default=False)
    # complete_1_game = models.BooleanField(default=False)
    # basic_output = models.BooleanField(default=False)
    # html_basics_1 = models.BooleanField(default=False)
    # css_basics = models.BooleanField(default=False)
    # html_basics_2 = models.BooleanField(default=False)
    # html_basics_3 = models.BooleanField(default=False)
    # html_basics_4 = models.BooleanField(default=False)
    # html_basics_5 = models.BooleanField(default=False)
    # respond_to_events = models.BooleanField(default=False)
    # to_do = models.BooleanField(default=False)
    # click = models.BooleanField(default=False)
    # keypress = models.BooleanField(default=False)
    # mouse_jump = models.BooleanField(default=False)
    # on_the_move = models.BooleanField(default=False)
    # motion_sickness = models.BooleanField(default=False)
    # show_an_understanding_of_pen = models.BooleanField(default=False)
    # functions = models.BooleanField(default=False)
    # sprites = models.BooleanField(default=False)
    # graphic_effects = models.BooleanField(default=False)
    # pow_boing = models.BooleanField(default=False)
    # background = models.BooleanField(default=False)
    # program_a_game = models.BooleanField(default=False)
    achievement_1 = models.BooleanField(default=False)
    achievement_2 = models.BooleanField(default=False)
    achievement_3 = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Code(models.Model):
    code = models.CharField(max_length=10)
    amount = models.IntegerField()

    def __str__(self):
        return self.code

class MentorCode(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.PROTECT)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.user.user.username

class LoginModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class UpdateModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
