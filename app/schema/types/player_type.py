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
    product_cards = graphene.List('app.schema.types.ProductCardType')
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

    def resolve_product_cards(self, info):
        product_cards =self.product_cards.through.objects.filter(player=self)
        return product_cards

    def resolve_hero(root, info):
        return root.hero

