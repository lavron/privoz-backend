from graphene_django import DjangoObjectType
from app.models.trader import Trader


class TraderType(DjangoObjectType):
    class Meta:
        model = Trader