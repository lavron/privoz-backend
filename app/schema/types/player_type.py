from graphene_django import DjangoObjectType
import graphene

from app.models import Player


class BasePlayerType(DjangoObjectType):
    class Meta:
        model = Player
        fields = [
            'id',
            'hero',
        ]

class PlayerType(DjangoObjectType):
    traders = graphene.List('app.schema.types.TraderForUserType')
    product_cards = graphene.List('app.schema.types.BaseProductCardType')
    hero = graphene.Field('app.schema.types.HeroType')

    class Meta:
        model = Player
        fields = [
            'id',
            'product_cards',
            'traders',
            'hero',
            'coins',
        ]

    def resolve_traders(root, info):
        return root.traders.all()

    def resolve_product_cards(root, info):
        return root.product_cards.all()

    def resolve_hero(root, info):
        return root.hero
