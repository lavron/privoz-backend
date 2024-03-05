from graphene_django import DjangoObjectType
from app.models import BaseEventCard


class EventCardType(DjangoObjectType):
    class Meta:
        model = BaseEventCard
        fields = [
            'id',
            'name',
            'name',
            'image',
            'effect',
            'target',
            'extra_profit',
        ]
