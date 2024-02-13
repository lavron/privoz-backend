import graphene
from graphene_django import DjangoObjectType
from app.models import Game, Player, Sector, ProductCard, EventCard


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


class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    players = graphene.List(PlayerType)
    sectors = graphene.List(SectorType)
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)

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


schema = graphene.Schema(query=Query)