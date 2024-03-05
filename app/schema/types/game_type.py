import graphene
from graphene_django import DjangoObjectType

from app.models import GameQueue, Game

from app.schema.types.event_card_type import EventCardType
from app.schema.types.player_type import PlayerType
from app.schema.types.product_card_type import ProductCardType
from app.schema.types.sector_type import SectorType


class GameQueueType(DjangoObjectType):
    class Meta:
        model = GameQueue
        fields = (
            'active_player_id', 'players_order_ids', 'phase')

    def resolve_phase(self, info):
        print("👉🏻self.phase", self.phase, type(self.phase))
        return self.phase


class GameStaticType(DjangoObjectType):
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)
    players = graphene.List(PlayerType)

    class Meta:
        model = Game
        fields = (
            'product_cards', 'sectors',
            'queue')


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
        return self.sectors.all()



    # def resolve_product_cards(self, info):
    #     return self.static.product_cards.all()
    #
    def resolve_players(self, info):
        return self.players.all()
