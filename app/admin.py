from django.contrib import admin

from app.models import Hero, Game, Trader, Player, Product, \
    BaseSector

admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(Product)
admin.site.register(BaseSector)
admin.site.register(Trader)
admin.site.register(Game, fields=['players_count', ])