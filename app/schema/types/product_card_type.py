from graphene_django import DjangoObjectType
from app.models import ProductCard


class ProductCardType(DjangoObjectType):
    class Meta:
        model = ProductCard
