from django.contrib import admin

from app.models import Player, EventCard, ProductCard, Sector, Game, Trader
from app.models.event_card import EventCardDeck
from app.models.product_card import ProductCardDeck

admin.site.register(Player,  exclude=('coins',))
admin.site.register(EventCard, exclude=('location',))
admin.site.register(ProductCard)
admin.site.register(Sector)
admin.site.register(Game)
admin.site.register(Trader)
admin.site.register(EventCardDeck)
admin.site.register(ProductCardDeck)