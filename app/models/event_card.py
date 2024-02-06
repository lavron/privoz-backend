from django.db import models
from .card import Card

LOCATION_CHOICES = [
    ("deck", "Deck"),
    ("hand", "Hand"),
    ("played", "Played"),
    ("discard", "Discard"),
]
FORTUNE_CHOICES = [
    ("positive", "Positive"),
    ("negative", "Negative"),
    ("neutral", "Neutral"),
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
    fortune = models.CharField(max_length=20, choices=FORTUNE_CHOICES)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES)
    item = models.CharField(max_length=20, choices=ITEM_CHOICES)

    # effects
    confiscation = models.BooleanField()
    protection = models.BooleanField()

    player_extra_profit = models.IntegerField()
    trader_extra_profit = models.IntegerField()
    product_extra_profit = models.IntegerField()
