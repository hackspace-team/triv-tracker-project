# Generated by Django 2.2.3 on 2019-09-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triv_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievementrecord',
            old_name='attention',
            new_name='achievement1',
        ),
        migrations.RenameField(
            model_name='achievementrecord',
            old_name='background',
            new_name='achievement2',
        ),
        migrations.RenameField(
            model_name='achievementrecord',
            old_name='basic_output',
            new_name='achievement3',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='click',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='complete_1_game',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='complete_1_level',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='control_flow',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='css_basics',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='functions',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='get_installed',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='graphic_effects',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='hear_ye',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='hello_world',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_basics_1',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_basics_2',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_basics_3',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_basics_4',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_basics_5',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='html_page',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='keypress',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='let_me_teach',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='lightning_talk',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='loops_1',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='loops_2',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='motion_sickness',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='mouse_jump',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='on_the_move',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='pair_up',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='pow_boing',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='program_a_game',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='respond_to_events',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='show_an_understanding_of_pen',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='sprites',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='strings',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='technical_mentor',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='to_do',
        ),
        migrations.RemoveField(
            model_name='achievementrecord',
            name='variables',
        ),
    ]