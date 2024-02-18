from django.db import models

from .hero import Hero


class Player(models.Model):
    hero = models.ForeignKey(Hero, related_name='player_in_games', on_delete=models.CASCADE, null=True)
    game = models.ForeignKey('Game', related_name='player_in_games', on_delete=models.CASCADE, null=True)

    trader = models.ForeignKey('Trader', related_name='player_in_games', on_delete=models.CASCADE, null=True)
    coins = models.IntegerField(default=0)

    is_ready = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class PlayerEventCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    event_card = models.ForeignKey('EventCard', on_delete=models.CASCADE)


class PlayerProductCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    product_card = models.ForeignKey('ProductCard', on_delete=models.CASCADE)
