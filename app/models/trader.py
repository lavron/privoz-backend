from django.db import models


class Trader(models.Model):
    sector = models.ForeignKey('Sector', related_name='trader_related', on_delete=models.CASCADE, blank=True, null=True)
    product_cards = models.ManyToManyField('ProductCard', blank=True, default=None)
    is_active = models.BooleanField(default=True)
    player = models.ForeignKey('Player', related_name='traders', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Trader ' + str(self.pk)

    @staticmethod
    def add(player_id, sector_id):
        trader = Trader.objects.create(player_id=player_id, sector_id=sector_id)
        return trader


