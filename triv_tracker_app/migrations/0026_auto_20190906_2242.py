# Generated by Django 2.2.3 on 2019-09-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0025_auto_20190906_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluserprofile',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
    ]