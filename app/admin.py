from django.contrib import admin

from app.models import Hero, Game, Trader, Player, Product, \
    BaseSector, Event
from import_export.admin import ImportExportModelAdmin
from .resources import BaseSectorResource, EventResource, ProductResource, HeroResource


class BaseSectorAdmin(ImportExportModelAdmin):
    resource_class = BaseSectorResource


class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource


class HeroAdmin(ImportExportModelAdmin):
    resource_class = HeroResource


admin.site.register(Player)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BaseSector, BaseSectorAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Trader)
admin.site.register(Game, fields=['players_count', ])
