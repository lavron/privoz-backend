from django.contrib import admin

from app.models import Player, EventCard, ProductCard, Sector, Game

admin.site.register(Player,  exclude=('coins',))
admin.site.register(EventCard, exclude=('location',))
admin.site.register(ProductCard)
admin.site.register(Sector)
admin.site.register(Game)