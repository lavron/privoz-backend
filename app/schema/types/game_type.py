import graphene
from graphene_django import DjangoObjectType

from app.schema.types.box_type import ProductCardType, EventCardType
from app.schema.types.player_type import PlayerType
from app.models import Game


class GameType(DjangoObjectType):
    product_cards_deck = graphene.List(ProductCardType)
    event_cards_deck = graphene.List(EventCardType)
    players = graphene.List(PlayerType)

    class Meta:
        model = Game
        fields = (
        'id', 'players', 'sectors',
        'product_cards_deck', 'event_cards_deck',
        'turn_order', 'current_turn_index',
        'current_phase')

    def resolve_product_cards_deck(self, info):
        return self.product_cards_deck.cards.all()

    def resolve_event_cards_deck(self, info):
        return self.event_cards_deck.cards.all()

    def resolve_players(self, info):
        return self.players.all()
