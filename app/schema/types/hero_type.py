from graphene_django import DjangoObjectType
from app.models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
