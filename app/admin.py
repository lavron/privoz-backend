from django.contrib import admin

from app.models import Hero, EventCard, ProductCard, Sector, Game, Trader, Player

admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(EventCard, name='Event Cards')
admin.site.register(ProductCard)
admin.site.register(Sector)
admin.site.register(Trader)
admin.site.register(Game, fields=['players_count', ])