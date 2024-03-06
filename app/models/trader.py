from django.db import models

from app.models import ProductCard


class Trader(models.Model):
    sector = models.ForeignKey('Sector', related_name='trader_related', on_delete=models.CASCADE, blank=True, null=True)
    product_cards = models.ManyToManyField('ProductCard', blank=True, default=None, related_name='trader_related')
    is_active = models.BooleanField(default=True)
    player = models.ForeignKey('Player', related_name='traders', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Trader ' + str(self.pk)

    @staticmethod
    def create(player_id, sector_id):
        trader = Trader.objects.create(
            player_id=player_id,
            sector_id=sector_id,
        )

        trader.save()
        return trader

    def add_product_cards(self, product_cards_ids):
        product_cards = ProductCard.objects.filter(id__in=product_cards_ids)

        self.product_cards.add(*product_cards)
        self.save()
        return self

