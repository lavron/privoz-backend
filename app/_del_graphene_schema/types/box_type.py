from app.models import Hero
from graphene_django import DjangoObjectType
import graphene

from app.models import Sector, ProductCard, EventCard


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector


class ProductCardType(DjangoObjectType):
    class Meta:
        model = ProductCard


class EventCardType(DjangoObjectType):
    class Meta:
        model = EventCard


class BoxType(graphene.ObjectType):
    heroes = graphene.List(HeroType)
    sectors = graphene.List(SectorType)
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)
