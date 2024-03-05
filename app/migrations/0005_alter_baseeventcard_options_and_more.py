# Generated by Django 5.0.2 on 2024-03-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_hero_event_card_protection_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseeventcard',
            options={'verbose_name': 'Event Card', 'verbose_name_plural': 'Event Cards'},
        ),
        migrations.AlterModelOptions(
            name='baseproductcard',
            options={'verbose_name': 'Product Card', 'verbose_name_plural': 'Product Cards'},
        ),
        migrations.AlterModelOptions(
            name='basesector',
            options={'verbose_name': 'Sector', 'verbose_name_plural': 'Sectors'},
        ),
        migrations.AlterField(
            model_name='gamequeue',
            name='phase',
            field=models.CharField(choices=[('hire_trader', 'Hire Trader Phase'), ('sales', 'Sales Phase'), ('paycheck', 'Paycheck Phase')], default=('hire_trader', 'Hire Trader Phase'), max_length=100),
        ),
    ]
