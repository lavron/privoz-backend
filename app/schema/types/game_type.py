import graphene
from graphene_django import DjangoObjectType

from app.models import GameQueue, Game

from app.schema.types.event_card_type import EventCardType
from app.schema.types.player_type import PlayerType
from app.schema.types.product_card_type import ProductCardType


class GameQueueType(DjangoObjectType):
    class Meta:
        model = GameQueue


class GameType(DjangoObjectType):
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)
    players = graphene.List(PlayerType)
    queue = graphene.Field(GameQueueType)

    class Meta:
        model = Game
        fields = (
            'id', 'players', 'sectors',
            'product_cards', 'event_cards',
            'queue')

    def resolve_product_cards(self, info):
        return self.product_cards.all()

    def resolve_event_cards_deck(self, info):
        return self.event_cards.all()

    def resolve_players(self, info):
        return self.players.all()
