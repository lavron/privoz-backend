import graphene
from graphene_django import DjangoObjectType

from app.models import GameQueue, Game, Sector
from app.schema.types.player_type import PlayerType, BasePlayerType
from app.schema.types.sector_type import SectorType


class GameQueueType(DjangoObjectType):
    class Meta:
        model = GameQueue
        fields = (
            'active_player_id', 'players_order_ids', 'phase')

    def resolve_phase(self, info):
        print("👉🏻self.phase", self.phase, type(self.phase))
        return self.phase


class BaseGameType(DjangoObjectType):
    players = graphene.List(BasePlayerType)

    class Meta:
        model = Game
        fields = (
            'id', 'players')


class GameType(DjangoObjectType):
    queue = graphene.Field(GameQueueType)
    sectors = graphene.List(SectorType)
    players = graphene.List(PlayerType)

    class Meta:
        model = Game
        fields = (
            'id', 'players', 'sectors',
            'queue')

    def resolve_sectors(self, info):
        return Sector.objects.filter(game=self)

    def resolve_players(self, info):
        return self.players.all()
