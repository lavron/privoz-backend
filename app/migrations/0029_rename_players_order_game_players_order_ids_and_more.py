# Generated by Django 5.0.1 on 2024-02-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_game_players_order_game_players_turn_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='players_order',
            new_name='players_order_ids',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='players_turn_index',
            new_name='players_order_index',
        ),
    ]