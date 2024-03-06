from graphene_django import DjangoObjectType
from app.models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'color', 'image', 'sector_bonus', 'event_protection']
