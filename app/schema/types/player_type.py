from graphene_django import DjangoObjectType
import graphene

from app.models import Player, ProductCard


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
        print("👉🏻self.__dict__", self.__dict__)
        product_cards = ProductCard.objects.filter(player=self)
        print("👉🏻product_cards", product_cards)
        for product_card in product_cards:
            print("👉🏻product_card", product_card.__dict__)
        return product_cards

    def resolve_hero(root, info):
        return root.hero

