from django.db import models
from .card import Card
from ..game_config import PRODUCT_IMAGE_PLACEHOLDER


# from .sector import Sector


class ProductCard(Card):
    is_legal = models.BooleanField(default=True)
    sector = models.ForeignKey('Sector', related_name='products', on_delete=models.CASCADE)
    sell_price = models.IntegerField()
    buy_price = models.IntegerField()

    image = models.CharField(max_length=100, blank=True, default=PRODUCT_IMAGE_PLACEHOLDER)
