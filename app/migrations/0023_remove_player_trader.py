# Generated by Django 5.0.1 on 2024-02-19 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_eventcard_location_remove_game_current_player_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='trader',
        ),
    ]