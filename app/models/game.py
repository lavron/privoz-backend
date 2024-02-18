from django.db import models

from app.models import Sector
from app.models.event_card import EventCardDeck
# from app.models.player import Player
from app.models.product_card import ProductCardDeck


class Game(models.Model):
    # players = models.ManyToManyField('Hero', related_name='games', through=Player)
    # players = models.ManyToManyField('Hero', related_name='games')
    product_cards_deck = models.ForeignKey(ProductCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    event_cards_deck = models.ForeignKey(EventCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    sectors = models.ManyToManyField(Sector, related_name='games')

    turn = models.IntegerField(default=0)
    current_player = models.ForeignKey('Player', related_name='current_games', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return 'Game ' + str(self.pk)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Game, self).save(*args, **kwargs)
        if is_new:
            self.create()

    def create(self):
        self.trader_capacity = self.players.count()
        self.product_cards_deck = ProductCardDeck.create_and_initialize()
        self.event_cards_deck = EventCardDeck.create_and_initialize()
        self.sectors.set(Sector.objects.all())
        self.save()
