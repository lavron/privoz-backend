from django.db import models

from .card import BaseCard
from ..game_config import PRODUCT_IMAGE_PLACEHOLDER


class Product(BaseCard):
    is_legal = models.BooleanField(default=True)
    sector = models.ForeignKey('BaseSector', related_name='products', on_delete=models.CASCADE)
    sell_price = models.IntegerField()
    buy_price = models.IntegerField()

    image = models.CharField(max_length=100, blank=True, default=PRODUCT_IMAGE_PLACEHOLDER)

    class Meta:
        verbose_name = "Product Card"
        verbose_name_plural = "Product Cards"


class ProductCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_card')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='product_card')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='product_card', null=True)
    trader = models.ForeignKey('Trader', on_delete=models.CASCADE, related_name='product_card', null=True)
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='product_card', null=True)

    is_discarded = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.product.name
