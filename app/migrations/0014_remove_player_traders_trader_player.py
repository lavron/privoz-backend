# Generated by Django 5.0.1 on 2024-02-15 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_game_event_cards_deck_game_product_cards_deck_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='traders',
        ),
        migrations.AddField(
            model_name='trader',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='traders', to='app.player'),
        ),
    ]