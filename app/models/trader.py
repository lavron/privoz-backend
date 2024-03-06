from django.db import models

from app.models import ProductCard


class Trader(models.Model):
    sector = models.ForeignKey('Sector', related_name='trader_related', on_delete=models.CASCADE, blank=True, null=True)
    product_cards = models.ManyToManyField('ProductCard', blank=True, default=None)
    is_active = models.BooleanField(default=True)
    player = models.ForeignKey('Player', related_name='traders', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Trader ' + str(self.pk)

    @staticmethod
    def create(player_id, sector_id, product_cards_ids):
        trader = Trader.objects.create(
            player_id=player_id,
            sector_id=sector_id,
        )
        product_cards = ProductCard.objects.filter(id__in=product_cards_ids)
        trader.product_cards.add(*product_cards)
        trader.save()
        return trader


