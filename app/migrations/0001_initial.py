# Generated by Django 5.0.1 on 2024-02-13 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField(db_default=models.Value(1), default=1)),
                ('location', models.CharField(choices=[('deck', 'Deck'), ('hand', 'Hand'), ('played', 'Played'), ('discard', 'Discard')], default='deck', max_length=20)),
                ('fortune', models.CharField(blank=True, choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=20)),
                ('target', models.CharField(blank=True, choices=[('player', 'Player'), ('sector', 'Sector'), ('trader', 'Trader')], max_length=20)),
                ('confiscation', models.BooleanField(blank=True, default=False)),
                ('protection', models.BooleanField(blank=True, default=False)),
                ('player_extra_profit', models.IntegerField(blank=True, null=True)),
                ('trader_extra_profit', models.IntegerField(blank=True, null=True)),
                ('product_extra_profit', models.IntegerField(blank=True, null=True)),
                ('product_extra_item', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, default='https://dummyimage.com/512/62929E/ffffff.png&text=+++EVENT', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('coins', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=20)),
                ('event_card_protection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_card_protection', to='app.eventcard')),
                ('premium_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='premium_sector', to='app.sector')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField(db_default=models.Value(1), default=1)),
                ('is_legal', models.BooleanField(default=True)),
                ('sell_price', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('image', models.CharField(blank=True, default='https://dummyimage.com/512/6ab555/ffffff.png&text=+PRODUCT', max_length=100)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.sector')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trader_capacity', models.IntegerField(default=2)),
                ('event_cards', models.ManyToManyField(related_name='games', to='app.eventcard')),
                ('players', models.ManyToManyField(related_name='games', to='app.player')),
                ('product_cards', models.ManyToManyField(related_name='games', to='app.productcard')),
                ('sectors', models.ManyToManyField(related_name='games', to='app.sector')),
            ],
        ),
    ]
