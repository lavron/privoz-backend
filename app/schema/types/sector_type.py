import graphene
from graphene_django import DjangoObjectType
from app.models import Sector, BaseSector


class BaseSectorType(DjangoObjectType):
    class Meta:
        model = BaseSector
        fields = (
            'id',
            'name',
        )


class SectorForProductCardType(DjangoObjectType):
    id = graphene.Int()
    name = graphene.String()

    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
        )

    def resolve_name(root, info):
        return root.sector.name

    def resolve_id(self, info):
        return self.id


class SectorType(DjangoObjectType):
    traders = graphene.List('app.schema.types.TraderForSectorType')
    id = graphene.Int()
    name = graphene.String()

    class Meta:
        model = Sector
        fields = (
            'id',
            'traders',
            'name',
        )

    def resolve_traders(self, info):
        return self.trader_related.all()

    def resolve_name(root, info):
        return root.sector.name
