from django.db import models
from .card import Card, Deck
from ..game_config import EVENT_IMAGE_PLACEHOLDER

LOCATION_CHOICES = [
    ("deck", "Deck"),
    ("hand", "Hand"),
    ("played", "Played"),
    ("discard", "Discard"),
]
FORTUNE_CHOICES = [
    ("positive", "Positive"),
    ("negative", "Negative"),
    # ("neutral", "Neutral"),
]
TARGET_CHOICES = [
    ("player", "Player"),
    ("sector", "Sector"),
    ("trader", "Trader"),
]
ITEM_CHOICES = [
    ("trader", "Trader"),
    ("product_card", "Product Card"),
]


class EventCard(Card):
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default="deck")
    fortune = models.CharField(max_length=20, choices=FORTUNE_CHOICES, blank=True)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, blank=True)

    # effects
    confiscation = models.BooleanField(blank=True, default=False)
    protection = models.BooleanField(blank=True, default=False)

    player_extra_profit = models.IntegerField(blank=True, null=True)
    trader_extra_profit = models.IntegerField(blank=True, null=True)
    product_extra_profit = models.IntegerField(blank=True, null=True)

    product_extra_item = models.IntegerField(blank=True, null=True)

    # trader_is_active = models.BooleanField(default=True)

    image = models.CharField(max_length=100, blank=True, default=EVENT_IMAGE_PLACEHOLDER)


class EventCardDeck(Deck):
    def __init__(self, *args, **kwargs):
        super().__init__(card_model=EventCard, *args, **kwargs)
        # self.save()

    def __str__(self):
        return 'Event Card Deck ' + str(self.pk)
