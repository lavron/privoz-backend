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
    product_cards_deck = models.ForeignKey(ProductCardDeck, on_delete=models.CASCADE, related_name='games', null=True)
    event_cards_deck = models.ForeignKey(EventCardDeck, on_delete=models.CASCADE, related_name='games', null=True)

    sectors = models.ManyToManyField(Sector, related_name='games', through='GameSector')

    active_player_id = models.IntegerField(null=True)
    players_order_ids = ArrayField(models.IntegerField(), default=list)
    players_order_index = models.IntegerField(default=0)

    current_phase = models.CharField(
        max_length=30,
        choices=PHASE_CHOICES,
        default='hire_trader',
    )

    def restart(self):
        self.players_order_index = 0
        self.current_phase = 'hire_trader'
        self.initialize_card_decks()
        for player in self.players.all():
            player.reset()
        self.save()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_game_resources()
            print(self.__dict__)

    def create_game_resources(self):
        self.set_trader_capacity()
        self.initialize_card_decks()
        self.assign_all_sectors()
        self.create_players()
        self.randomize_players_order()
        self.set_active_first_player()
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
            self.players_order_ids.append(player.pk)

    def randomize_players_order(self):
        random.shuffle(self.players_order_ids)

    def set_active_first_player(self):
        self.active_player_id = self.players_order_ids[0]

    def end_turn(self):
        print("👉🏻end_turn")
        self.players_order_index += 1
        print("👉🏻self.players_order_index", self.players_order_index)
        if self.players_order_index == len(self.players_order_ids):
            self.players_order_index = 0
            print("👉🏻reset")
            self.move_to_next_phase()
        self.save()

    def move_to_next_phase(self):
        self.current_phase = PHASE_ORDER[self.current_phase]

    def __str__(self):
        return 'Game ' + str(self.pk)
