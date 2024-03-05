from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core import serializers

from privoz.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Loads model data from JSON file'

    def handle(self, *args, **kwargs):
        path = BASE_DIR / 'app' / 'management' / 'commands' / 'json'
        for model in ['BaseSector', 'BaseEventCard', 'BaseProductCard', 'Hero']:
            with open(f'{path}/{model}.json', 'r') as f:
                data = f.read()
                # print("👉🏻data", data)

                for deserialized_object in serializers.deserialize("json", data):
                    try:
                        deserialized_object.save()
                        print("👉🏻deserialized_object", deserialized_object)
                    except ValidationError as e:
                        print(f"Validation error for {model}: {e}")
                    except Exception as e:
                        print(f"Unexpected error for {model}: {e}")