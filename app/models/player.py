from django.db import models

from .hero import Hero
from ..game_config import INITIAL_COINS


class Player(models.Model):
    hero = models.ForeignKey(Hero, related_name='players', on_delete=models.CASCADE, null=True)
    game = models.ForeignKey('Game', related_name='players', on_delete=models.CASCADE, null=True)

    event_cards = models.ManyToManyField('EventCard')
    product_cards = models.ManyToManyField('ProductCard')
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.hero.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.coins = INITIAL_COINS

    def reset(self):
        self.coins = 0
        self.event_cards.clear()
        self.product_cards.clear()
        self.save()

    def end_turn(self):
        self.game.end_turn()

    def take_product_cards(self, count):
        product_cards = self.game.product_cards.draw_cards(count)
        for product_card in product_cards:
            self.product_cards.add(product_card)
        self.save()
