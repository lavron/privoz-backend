# Generated by Django 5.0.1 on 2024-02-18 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_productcard_location_alter_eventcard_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.RemoveField(
            model_name='player',
            name='color',
        ),
        migrations.RemoveField(
            model_name='player',
            name='event_card_protection',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='premium_sector',
        ),
        migrations.AddField(
            model_name='game',
            name='current_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_games', to='app.player'),
        ),
        migrations.AddField(
            model_name='game',
            name='turn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(db_default=models.Value(14), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_in_games', to='app.game'),
        ),
        migrations.AddField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='trader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_in_games', to='app.trader'),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=20)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('event_card_protection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_card_protection', to='app.eventcard')),
                ('premium_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='premium_sector', to='app.sector')),
            ],
        ),
    ]
