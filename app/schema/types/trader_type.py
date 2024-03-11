import graphene
from graphene_django import DjangoObjectType
from app.models import Trader



class TraderForUserType(DjangoObjectType):
    class Meta:
        model = Trader
        fields = (
            'id',
        )


class TraderForSectorType(DjangoObjectType):
    product_cards = graphene.List('app.schema.types.ProductCardType')

    class Meta:
        model = Trader
        fields = (
            'id',
            'product_cards',
            'player',
        )

    def resolve_product_cards(self, info):
        return self.product_cards.all()
