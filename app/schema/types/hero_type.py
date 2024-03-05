from graphene_django import DjangoObjectType
from app.models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'color', 'image', 'premium_sector', 'event_card_protection']
