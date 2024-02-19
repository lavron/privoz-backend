import random

from django.db import models

from app.models import Sector, Hero
from app.models.event_card import EventCardDeck
from app.models.player import Player
from app.models.product_card import ProductCardDeck


class Game(models.Model):
    players_count = models.IntegerField(default=2)

    # players = models.ManyToManyField('Hero', related_name='games', through=Player)
    product_cards_deck = models.ForeignKey(ProductCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    event_cards_deck = models.ForeignKey(EventCardDeck, on_delete=models.CASCADE, related_name='games', null=True)

    sectors = models.ManyToManyField(Sector, related_name='games', through='GameSector')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_game_resources()

    def create_game_resources(self):
        self.set_trader_capacity()
        self.initialize_card_decks()
        self.assign_all_sectors()
        self.create_players()
        self.save()

    def set_trader_capacity(self):
        self.trader_capacity = self.players_count

    def initialize_card_decks(self):
        self.product_cards_deck = ProductCardDeck.create_and_initialize()
        self.event_cards_deck = EventCardDeck.create_and_initialize()

    def assign_all_sectors(self):
        self.sectors.set(Sector.objects.all())

    def create_players(self):
        heroes = list(Hero.objects.all())
        random.shuffle(heroes)
        heroes = heroes[:self.players_count]
        for hero in heroes:
            player = Player(hero=hero, game=self)
            player.save()

    def __str__(self):
        return 'Game ' + str(self.pk)

# https://github.com/tsaglam/Carcassonne/tree/master/src/main/java/carcassonne/model
#  https://github.com/seansegal/tincisnotcatan/blob/master/src/main/java/edu/brown/cs/actions/BuyDevelopmentCard.java#L18
