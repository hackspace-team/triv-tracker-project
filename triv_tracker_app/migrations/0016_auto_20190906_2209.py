# Generated by Django 2.2.3 on 2019-09-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0015_auto_20190906_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]