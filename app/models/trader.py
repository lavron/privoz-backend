from django.db import models


class Trader(models.Model):
    sector = models.ForeignKey('Sector', related_name='traders', on_delete=models.CASCADE)
    products = models.ManyToManyField('ProductCard', related_name='traders')
    product_cards = models.ManyToManyField('ProductCardInDeck', related_name='traders', blank=True, default=None)
    is_active = models.BooleanField(default=True)
    player = models.ForeignKey('Player', related_name='traders', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=1)

    def __str__(self):
        return 'Trader ' + str(self.pk)