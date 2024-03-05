from django.contrib import admin

from app.models import Hero, Game, Trader, Player, BaseEventCard, BaseProductCard, \
    BaseSector

admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(BaseEventCard)
admin.site.register(BaseProductCard)
admin.site.register(BaseSector)
admin.site.register(Trader)
admin.site.register(Game, fields=['players_count', ])