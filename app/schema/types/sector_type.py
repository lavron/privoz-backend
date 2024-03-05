import graphene
from graphene_django import DjangoObjectType
from app.models import Sector
from app.schema.types import TraderForSectorType


class SectorType(DjangoObjectType):
    traders = graphene.List(TraderForSectorType)
    class Meta:
        model = Sector
        fields = ['name', 'description', 'traders']

    def resolve_traders(self, info):
        return self.traders.all()
