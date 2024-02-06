from django.db import models
from app.game_config import INITIAL_COINS


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coins = models.IntegerField(default=INITIAL_COINS)
    color = models.CharField(max_length=20)