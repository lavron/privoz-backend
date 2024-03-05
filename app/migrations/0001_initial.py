# Generated by Django 5.0.2 on 2024-03-05 12:53

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEventCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('quantity_in_deck', models.IntegerField(default=1)),
                ('effect', models.CharField(blank=True, choices=[('confiscation', 'Confiscation'), ('protection', 'Protection'), ('profit', 'Profit'), ('extra_item', 'Extra Item')], max_length=20)),
                ('target', models.CharField(blank=True, choices=[('player', 'Player'), ('sector', 'Sector'), ('trader', 'Trader'), ('product', 'Product')], max_length=20)),
                ('extra_profit', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, default='https://dummyimage.com/512/62929E/ffffff.png&text=+++EVENT', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaseProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('quantity_in_deck', models.IntegerField(default=1)),
                ('is_legal', models.BooleanField(default=True)),
                ('sell_price', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('image', models.CharField(blank=True, default='https://dummyimage.com/512/6ab555/ffffff.png&text=+PRODUCT', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaseSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_discarded', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_card', to='app.baseeventcard')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_count', models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(4)])),
                ('trader_capacity', models.IntegerField(default=2)),
                ('event_cards', models.ManyToManyField(related_name='game', through='app.EventCard', to='app.baseeventcard')),
            ],
        ),
        migrations.AddField(
            model_name='eventcard',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_card', to='app.game'),
        ),
        migrations.CreateModel(
            name='GameQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_player_id', models.IntegerField(null=True)),
                ('players_order_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('players_order_index', models.IntegerField(default=0)),
                ('phase', models.CharField(choices=[('hire_trader', 'Hire Trader Phase'), ('take_event_card', 'Take Event Card Phase'), ('buy_products', 'Buy Products Phase'), ('reveal_week_card', 'Week Card Reveal Phase'), ('reveal_negative_card', 'Negative Card Reveal Phase'), ('sales', 'Sales Phase'), ('play_event_card', 'Play Event Card Phase'), ('paycheck', 'Paycheck Phase')], default=('hire_trader', 'Hire Trader Phase'), max_length=30)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_queue', to='app.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='queue',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_related', to='app.gamequeue'),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=20)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('event_card_protection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_card_protection', to='app.eventcard')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_discarded', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_card', to='app.baseproductcard')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_card', to='app.game')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(default=0)),
                ('event_cards', models.ManyToManyField(to='app.eventcard')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='app.game')),
                ('hero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='app.hero')),
                ('product_cards', models.ManyToManyField(to='app.productcard')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='product_cards',
            field=models.ManyToManyField(related_name='game', through='app.ProductCard', to='app.baseproductcard'),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector', to='app.game')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector', to='app.basesector')),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='premium_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='premium_sector', to='app.sector'),
        ),
        migrations.AddField(
            model_name='game',
            name='sectors',
            field=models.ManyToManyField(related_name='game', through='app.Sector', to='app.basesector'),
        ),
        migrations.AddField(
            model_name='baseproductcard',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cards', to='app.sector'),
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='traders', to='app.player')),
                ('product_cards', models.ManyToManyField(blank=True, default=None, to='app.productcard')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trader_related', to='app.sector')),
            ],
        ),
        migrations.AddField(
            model_name='sector',
            name='traders',
            field=models.ManyToManyField(blank=True, default=None, related_name='sector_related', to='app.trader'),
        ),
    ]
