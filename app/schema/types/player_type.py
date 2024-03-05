from graphene_django import DjangoObjectType
import graphene

from app.models import Player


class PlayerType(DjangoObjectType):
    hero = graphene.Field('app.schema.types.HeroType')
    traders = graphene.Field('app.schema.types.TraderForUserType')

    class Meta:
        model = Player

    def resolve_hero(root, info):
        return root.hero


    def resolve_traders(root, info):
        return root.traders.all()
