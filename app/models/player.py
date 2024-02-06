from django.db import models
from app.game_config import INITIAL_COINS


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coins = models.IntegerField(default=0)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name