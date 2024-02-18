from django.db import models
from .card import Card, Deck, CardInDeck
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
]
ITEM_CHOICES = [
    ("trader", "Trader"),
    ("product_card", "Product Card"),
]


class EventCard(Card):
    fortune = models.CharField(max_length=20, choices=FORTUNE_CHOICES, blank=True)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, blank=True)

    # effects
    confiscation = models.BooleanField(blank=True, default=False)
    protection = models.BooleanField(blank=True, default=False)

    player_extra_profit = models.IntegerField(blank=True, null=True)
    trader_extra_profit = models.IntegerField(blank=True, null=True)
    product_extra_profit = models.IntegerField(blank=True, null=True)

    product_extra_item = models.IntegerField(blank=True, null=True)

    image = models.CharField(max_length=100, blank=True, default=EVENT_IMAGE_PLACEHOLDER)


class EventCardDeck(Deck):
    cards = models.ManyToManyField(EventCard, through='EventCardInDeck')

    def __init__(self, *args, **kwargs):
        super().__init__(card_model=EventCard, card_in_deck_model=EventCardInDeck, *args, **kwargs)

    def save(self, *args, **kwargs):
        is_new = not self.pk
        print("👉🏻is_new", is_new)
        super().save(*args, **kwargs)


class EventCardInDeck(CardInDeck):
    card = models.ForeignKey(EventCard, on_delete=models.CASCADE)
    deck = models.ForeignKey(EventCardDeck, on_delete=models.CASCADE, related_name='cardindeck_set')


    def __str__(self):
        return f"{self.card.name} in {self.deck.id}"
