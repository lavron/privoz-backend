from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core import serializers
from django.apps import apps

from app.models import BaseSector, Event
from privoz.settings import BASE_DIR
import json
import pdb
from django.forms.models import model_to_dict


class Command(BaseCommand):
    SECTOR_FIELDS = ['sector', 'premium_sector']
    EVENT_FIELDS = ['event_card_protection', ]
    help = 'Loads model data from JSON file'

    MODEL_MAPPING = {
        'BaseSector': 'BaseSector',
        'BaseEventCard': 'Event',
        'BaseProductCard': 'Product',
        'Hero': 'Hero',
    }

    def update_sector_fields(self, deserialized_dict, fields):
        for field in fields:
            if field in deserialized_dict:
                sector_id = deserialized_dict[field]
                deserialized_dict[field] = BaseSector.objects.get(id=sector_id)

    def update_event_fields(self, deserialized_dict, fields):
        for field in fields:
            if field in deserialized_dict:
                event_id = deserialized_dict[field]
                deserialized_dict[field] = Event.objects.get(id=event_id)

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
                # pdb.set_trace()
                for deserialized_object in serializers.deserialize("json", data):
                    deserialized_dict = model_to_dict(deserialized_object.object)
                    print("👉🏻deserialized_dict", deserialized_dict)

                    self.update_sector_fields(deserialized_dict, self.SECTOR_FIELDS)
                    self.update_event_fields(deserialized_dict, self.EVENT_FIELDS)
                    new_instance = NewModel.objects.create(**deserialized_dict)
                    new_instance.save()
