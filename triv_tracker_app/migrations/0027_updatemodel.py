# Generated by Django 2.2.3 on 2019-09-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0026_auto_20190906_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
