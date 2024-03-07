import graphene
from graphene_django import DjangoObjectType
from app.models import Sector, BaseSector
from app.schema.types import TraderForSectorType


class BaseSectorType(DjangoObjectType):
    class Meta:
        model = BaseSector
        fields = (
            'id',
            'name',
        )


class SectorType(DjangoObjectType):
    traders = graphene.List(TraderForSectorType)
    id = graphene.Int()
    name = graphene.String()

    class Meta:
        model = Sector
        fields = (
            'id',
            'traders',
        )

    def resolve_traders(root, info):
        return root.traders.all()

    def resolve_name(root, info):
        return root.sector.name
