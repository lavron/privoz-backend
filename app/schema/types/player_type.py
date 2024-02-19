from graphene_django import DjangoObjectType
import graphene

from app.schema.types.trader_type import TraderType
from app.models import Player


class PlayerType(DjangoObjectType):
    traders = graphene.List(TraderType)

    class Meta:
        model = Player

    def resolve_traders(root, info):
        return root.traders.all()