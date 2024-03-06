from graphene_django import DjangoObjectType
from app.models import Product, ProductCard


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        exclude = ('game', 'quantity_in_deck')

class ProductCardType(DjangoObjectType):
    class Meta:
        model = ProductCard
        fields = (
            'id',
            'product',
        )

    def resolve_product(root, info):
        return root.product