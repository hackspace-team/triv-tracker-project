# Generated by Django 2.2.3 on 2019-09-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0018_auto_20190906_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='last_achievement_name',
            field=models.CharField(default='HI', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_achievement_name',
            field=models.CharField(default='HI', max_length=200),
        ),
    ]