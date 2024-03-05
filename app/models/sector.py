from django.db import models
from django.utils.functional import cached_property


class Sector(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SectorInGame(models.Model):
    sector = models.ForeignKey(Sector, related_name='sector_in_game', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', related_name='sector_in_game', on_delete=models.CASCADE)
    traders = models.ManyToManyField('Trader', related_name='sector_in_game', blank=True, default=None)

    @cached_property
    def capacity(self):
        return self.game.players_count
