from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core import serializers
from django.apps import apps
from privoz.settings import BASE_DIR
import json


class Command(BaseCommand):
    help = 'Loads model data from JSON file'

    MODEL_MAPPING = {
        'BaseSector': 'BaseSector',
        'BaseEventCard': 'Event',
        'BaseProductCard': 'Product',
        'Hero': 'Hero',
    }


    def handle(self, *args, **kwargs):
        path = BASE_DIR / 'app' / 'management' / 'commands' / 'json'

        for old_model, new_model in self.MODEL_MAPPING.items():
            with open(f'{path}/{old_model}.json', 'r') as f:
                data = json.load(f)

                # Change the "old_model" identifiers to "new_model"
                for item in data:
                    if item['model'] == f'app.{old_model.lower()}':
                        item['model'] = f'app.{new_model.lower()}'

                # Cast the data back to str for deserialization
                data = json.dumps(data)

                NewModel = apps.get_model(app_label='app', model_name=new_model)

                for deserialized_object in serializers.deserialize("json", data):
                    deserialized_dict = deserialized_object.object.__dict__

                    deserialized_dict.pop('_state', None)

                    new_instance = NewModel(**deserialized_dict)
