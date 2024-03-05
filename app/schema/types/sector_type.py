import graphene
from graphene_django import DjangoObjectType
from app.models import Sector, BaseSector
from app.schema.types import TraderForSectorType


class SectorType(DjangoObjectType):
    traders = graphene.List(TraderForSectorType)
    id = graphene.Int()
    class Meta:
        model = BaseSector
        fields = (
            'id',
            'name',
        )

    def resolve_id(self, info):
        return self.id

    def resolve_traders(self, info):
        return self.traders.all()

