from graphene_django import DjangoObjectType
from app.models import BaseProductCard, ProductCard


class BaseProductCardType(DjangoObjectType):
    class Meta:
        model = BaseProductCard
        exclude = ('game', 'quantity_in_deck')