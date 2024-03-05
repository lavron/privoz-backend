from django.core.management.base import BaseCommand
from django.core import serializers
from app.models import BaseSector, BaseEventCard, BaseProductCard, Hero


class Command(BaseCommand):
    help = 'Export model data to JSON file'

    def handle(self, *args, **kwargs):

        data = serializers.serialize("json", BaseSector.objects.all())
        with open('json/BaseSector.json', 'w') as f:
            f.write(data)

        data = serializers.serialize("json", BaseEventCard.objects.all())
        with open('json/BaseEventCard.json', 'w') as f:
            f.write(data)

        data = serializers.serialize("json", BaseProductCard.objects.all())
        with open('json/BaseProductCard.json', 'w') as f:
            f.write(data)

        data = serializers.serialize("json", Hero.objects.all())
        with open('json/Hero.json', 'w') as f:
            f.write(data)
