from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.game_config import PHASE_CHOICES, PHASE_ORDER, MAX_PLAYERS

from django.core.validators import MaxValueValidator

from app.models.sector import BaseSector
from app.services import GameResourcesCreator
from app.services.game_engine import GameEngine


class Game(models.Model):
    players_count = models.IntegerField(default=2, validators=[MaxValueValidator(MAX_PLAYERS)])
    trader_capacity = models.IntegerField(default=2)

    product_cards = models.ManyToManyField('Product', related_name='game', through='ProductCard')
    sectors = models.ManyToManyField(BaseSector, through='Sector', related_name='game')

    queue = models.OneToOneField('GameQueue', on_delete=models.CASCADE, related_name='game_related', null=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            GameResourcesCreator.create(self)
            self.queue.init()

    def __str__(self):
        return 'Game ' + str(self.pk)

    @property
    def active_player(self):
        return self.players.get(pk=self.queue.active_player_id)


class GameQueue(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_queue')

    active_player_id = models.IntegerField(null=True)
    players_order_ids = ArrayField(models.IntegerField(), default=list)
    players_order_index = models.IntegerField(default=0)

    phase = models.CharField(
        max_length=100,
        choices=PHASE_CHOICES,
        default=PHASE_CHOICES[0],
        null=True
    )

    def init(self):
        engine = GameEngine(self.game)
        engine.handle_phase()
        self.save()

    def next_turn(self):
        self.players_order_index += 1
        if self.players_order_index == len(self.players_order_ids):
            self.next_phase()
        else:
            self.active_player_id = self.players_order_ids[self.players_order_index]
            self.save()
            engine = GameEngine(self.game)
            engine.handle_phase()

    def next_phase(self):
        self.players_order_index = 0
        self.active_player_id = self.players_order_ids[self.players_order_index]
        self.phase = PHASE_ORDER[self.phase]
        self.save()
        engine = GameEngine(self.game)
        engine.handle_phase()


    def reset(self):
        self.phase = PHASE_CHOICES[0][0]
        self.players_order_index = 0
        self.active_player_id = self.players_order_ids[0]
        self.save()
        self.game.save()
