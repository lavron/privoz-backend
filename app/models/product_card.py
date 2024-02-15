from django.db import models
from .card import Card, Deck, CardInDeck
from ..game_config import PRODUCT_IMAGE_PLACEHOLDER


class ProductCard(Card):
    is_legal = models.BooleanField(default=True)
    sector = models.ForeignKey('Sector', related_name='products', on_delete=models.CASCADE)
    sell_price = models.IntegerField()
    buy_price = models.IntegerField()

    image = models.CharField(max_length=100, blank=True, default=PRODUCT_IMAGE_PLACEHOLDER)


class ProductCardDeck(Deck):
    cards = models.ManyToManyField(ProductCard, through='ProductCardInDeck')

    def __init__(self, *args, **kwargs):
        super().__init__(card_model=ProductCard, card_in_deck_model=ProductCardInDeck, *args, **kwargs)


class ProductCardInDeck(CardInDeck):
    card = models.ForeignKey(ProductCard, on_delete=models.CASCADE)
    deck = models.ForeignKey(ProductCardDeck, on_delete=models.CASCADE, related_name='cardindeck_set')

    def __str__(self):
        return f"{self.card.name} in deck {self.deck.id}"
