from django.db import models
from app.game_config import INITIAL_COINS


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coins = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    premium_sector = models.ForeignKey('Sector', related_name='premium_sector', on_delete=models.CASCADE, null=True)
    event_card_protection = models.ForeignKey('EventCard', related_name='event_card_protection', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name