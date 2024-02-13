import graphene
from graphene_django import DjangoObjectType
from app.models import Game, Player, Sector, ProductCard, EventCard, Trader
from app.models.event_card import EventCardDeck
from app.models.product_card import ProductCardDeck


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector


class ProductCardType(DjangoObjectType):
    class Meta:
        model = ProductCard


class EventCardType(DjangoObjectType):
    class Meta:
        model = EventCard


class TraderCardType(DjangoObjectType):
    class Meta:
        model = Trader

class EventCardDeckType(DjangoObjectType):
    class Meta:
        model = EventCardDeck

class ProductCardDeckType(DjangoObjectType):
    class Meta:
        model = ProductCardDeck



class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    players = graphene.List(PlayerType)
    sectors = graphene.List(SectorType)
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)
    traders = graphene.List(TraderCardType)
    event_card_decks = graphene.List(EventCardDeckType)
    product_card_decks = graphene.List(ProductCardDeckType)

    def resolve_game(self, info, pk, **kwargs):
        return Game.objects.get(pk=pk)

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_sectors(self, info, **kwargs):
        return Sector.objects.all()

    def resolve_product_cards(self, info, **kwargs):
        return ProductCard.objects.all()

    def resolve_event_cards(self, info, **kwargs):
        return EventCard.objects.all()

    def resolve_traders(self, info, **kwargs):
        return Trader.objects.all()

    def resolve_event_card_decks(self, info, **kwargs):
        return EventCardDeck.objects.all()

    def resolve_product_card_decks(self, info, **kwargs):
        return ProductCardDeck.objects.all()


schema = graphene.Schema(query=Query)