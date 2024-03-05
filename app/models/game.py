import random

from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.game_config import PHASE_CHOICES, PHASE_ORDER, MAX_PLAYERS

from app.models.player import Player
from app.models.product_card import BaseProductCard, ProductCard
from app.models.event_card import BaseEventCard, EventCard
from app.models.sector import Sector, SectorInGame
from django.core.validators import MaxValueValidator


class Game(models.Model):
    players_count = models.IntegerField(default=2, validators=[MaxValueValidator(MAX_PLAYERS)])

    product_cards = models.ManyToManyField(BaseProductCard, related_name='game', through=ProductCard)
    event_cards = models.ManyToManyField(BaseEventCard, related_name='game', through=EventCard)
    sectors = models.ManyToManyField(Sector, through='SectorInGame', related_name='game')

    active_player_id = models.IntegerField(null=True)
    players_order_ids = ArrayField(models.IntegerField(), default=list)
    players_order_index = models.IntegerField(default=0)

    trader_capacity = models.IntegerField(default=2)

    current_phase = models.CharField(
        max_length=30,
        choices=PHASE_CHOICES,
        default=PHASE_CHOICES[0],
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_game_resources()
            print(self.__dict__)

    def create_cards(self, card_model):
        card_bases = card_model.objects.all()
        for card_base in card_bases:
            for _ in range(card_base.quantity_in_deck):
                CardInGame.objects.create(card=card_base, game=self)

    def create_sectors(self):
        sectors = Sector.objects.all()
        for sector in sectors:
            SectorInGame.objects.create(sector=sector, game=self)

    def create_game_resources(self):
        self.trader_capacity = self.players_count
        self.create_cards(ProductCard)
        self.create_cards(EventCard)
        self.create_sectors()
        self.create_players()
        self.save()

    def create_players(self):
        from .hero import Hero
        heroes = list(Hero.objects.all())
        random.shuffle(heroes)
        heroes = heroes[:self.players_count]
        for hero in heroes:
            player = Player(hero=hero, game=self)
            player.save()
            self.players_order_ids.append(player.pk)
        random.shuffle(self.players_order_ids)
        self.active_player_id = self.players_order_ids[0]

    def end_turn(self):
        self.players_order_index += 1
        if self.players_order_index == len(self.players_order_ids):
            self.players_order_index = 0
            self.move_to_next_phase()
        self.active_player_id = self.players_order_ids[self.players_order_index]
        self.save()

    def move_to_next_phase(self):
        self.current_phase = PHASE_ORDER[self.current_phase]

    def __str__(self):

        return 'Game ' + str(self.pk)
