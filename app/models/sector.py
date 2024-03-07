from django.db import models


class BaseSector(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"


class Sector(models.Model):
    sector = models.ForeignKey(BaseSector, related_name='sector', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', related_name='sector', on_delete=models.CASCADE)
    traders = models.ManyToManyField('Trader', related_name='sector_related', blank=True, default=None)
