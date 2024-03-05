from django.db import models
from .card import BaseCard
from ..game_config import EVENT_IMAGE_PLACEHOLDER

FORTUNE_CHOICES = [
    ("positive", "Positive"),
    ("negative", "Negative"),
    # ("neutral", "Neutral"),
]
TARGET_CHOICES = [
    ("player", "Player"),
    ("sector", "Sector"),
    ("trader", "Trader"),
    ("product", "Product"),
]
ITEM_CHOICES = [
    ("trader", "Trader"),
    ("product_card", "Product Card"),
]

EFFECT_CHOICES = [
    ("confiscation", "Confiscation"),
    ("protection", "Protection"),
    ("profit", "Profit"),
    ("extra_item", "Extra Item"),
]


class BaseEventCard(BaseCard):
    effect = models.CharField(max_length=20, choices=EFFECT_CHOICES, blank=True)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, blank=True)
    extra_profit = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, default=EVENT_IMAGE_PLACEHOLDER)


class EventCard(models.Model):
    card = models.ForeignKey(BaseEventCard, on_delete=models.CASCADE, related_name='event_card')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='event_card')

    is_discarded = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
