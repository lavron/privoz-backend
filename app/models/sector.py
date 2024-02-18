from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GameSector(models.Model):
    sector = models.ForeignKey(Sector, related_name='game_sector_instances', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', related_name='game_sector_instances', on_delete=models.CASCADE)
