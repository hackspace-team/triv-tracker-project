# Generated by Django 2.2.3 on 2019-09-06 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0020_auto_20190906_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluserprofile',
            name='last_achievement_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_achievement_id',
        ),
    ]