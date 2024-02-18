from django.contrib import admin

from app.models import Hero, EventCard, ProductCard, Sector, Game, Trader, Player
from app.models.event_card import EventCardDeck
from app.models.product_card import ProductCardDeck

admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(EventCard, exclude=('location',))
admin.site.register(ProductCard)
admin.site.register(Sector)
admin.site.register(Game, exclude=('turn','current_player'))
admin.site.register(Trader)
admin.site.register(EventCardDeck)
admin.site.register(ProductCardDeck)