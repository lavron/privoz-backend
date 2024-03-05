from django.db import models

from .card import BaseCard
from ..game_config import PRODUCT_IMAGE_PLACEHOLDER


class BaseProductCard(BaseCard):
    is_legal = models.BooleanField(default=True)
    sector = models.ForeignKey('Sector', related_name='product_cards', on_delete=models.CASCADE)
    sell_price = models.IntegerField()
    buy_price = models.IntegerField()

    image = models.CharField(max_length=100, blank=True, default=PRODUCT_IMAGE_PLACEHOLDER)


class ProductCard(models.Model):
    card = models.ForeignKey(BaseProductCard, on_delete=models.CASCADE, related_name='product_card')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='product_card')

    is_discarded = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
