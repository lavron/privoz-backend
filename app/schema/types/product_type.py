from graphene_django import DjangoObjectType
from app.models import Product, ProductCard, Sector
from app.schema.types.sector_type import SectorForProductCardType
import graphene

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        exclude = ('game', 'quantity_in_deck', 'players', 'product_card', 'sector')


class ProductCardType(DjangoObjectType):
    sector = graphene.Field(SectorForProductCardType)
    class Meta:
        model = ProductCard
        fields = (
            'id',
            'product',
            'sector'
        )

    def resolve_product(self, info):
        return self.product

    def resolve_sector(root, info):
        sector = root.sector
        return sector
