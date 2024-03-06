from import_export import resources
from .models import BaseSector, Event, Product, Hero


class BaseSectorResource(resources.ModelResource):
    class Meta:
        model = BaseSector


class EventResource(resources.ModelResource):
    class Meta:
        model = Event


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class HeroResource(resources.ModelResource):
    class Meta:
        model = Hero