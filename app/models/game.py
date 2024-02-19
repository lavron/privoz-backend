import random

from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.game_config import INITIAL_COINS, PHASE_CHOICES, PHASE_ORDER
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

    turn_order = ArrayField(
        models.IntegerField(),
        default=list,
    )
    current_phase = models.CharField(
        max_length=30,
        choices=PHASE_CHOICES,
        default='hire_trader',
    )
    current_turn_index = models.IntegerField(default=0)


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
        self.create_turn_order()
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
            player.coins = INITIAL_COINS
            player.save()

    def create_turn_order(self):
        self.turn_order = list(range(self.players_count))
        random.shuffle(self.turn_order)


    def end_turn(self):
        # If current player is the last in turn order, move to next phase and reset turn_index
        if self.current_turn_index == len(self.turn_order) - 1:
            self.move_to_next_phase()
            self.reset_current_turn_index()
        else:
            self.current_turn_index += 1

        self.save()

    def move_to_next_phase(self):
        self.current_phase = PHASE_ORDER[self.current_phase]

    def reset_current_turn_index(self):
        self.current_turn_index = 0


    def __str__(self):
        return 'Game ' + str(self.pk)

# https://github.com/tsaglam/Carcassonne/tree/master/src/main/java/carcassonne/model
#  https://github.com/seansegal/tincisnotcatan/blob/master/src/main/java/edu/brown/cs/actions/BuyDevelopmentCard.java#L18
