# app/management/commands/clean_models.py

from django.core.management.base import BaseCommand
from app.models import *


class Command(BaseCommand):
    help = 'Delete all objects of specified models'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        BaseSector.objects.all().delete()
        Hero.objects.all().delete()
        Player.objects.all().delete()
        Trader.objects.all().delete()
        Sector.objects.all().delete()
        ProductCard.objects.all().delete()
        Game.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data cleaned successfully'))