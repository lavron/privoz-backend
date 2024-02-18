from django.db import models

from app.models import Sector, Hero
from app.models.event_card import EventCardDeck
from app.models.player import Player
from app.models.product_card import ProductCardDeck


class Game(models.Model):
    players_count = models.IntegerField(default=0)
    players = models.ManyToManyField('Hero', related_name='games', through=Player)
    product_cards_deck = models.ForeignKey(ProductCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    event_cards_deck = models.ForeignKey(EventCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    sectors = models.ManyToManyField(Sector, related_name='games')
    game_sectors = models.ManyToManyField(Sector, related_name='sector_games', through='GameSector')

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
        # get first 'players_count' heroes and create players
        heroes = Hero.objects.all()[:self.players_count]
        for hero in heroes:
            player = Player(hero=hero, game=self)
            player.save()

        self.save()


# https://github.com/tsaglam/Carcassonne/tree/master/src/main/java/carcassonne/model
#  https://github.com/seansegal/tincisnotcatan/blob/master/src/main/java/edu/brown/cs/actions/BuyDevelopmentCard.java#L18