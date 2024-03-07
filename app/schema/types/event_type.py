from graphene_django import DjangoObjectType
from app.models import Event


class EventCardType(DjangoObjectType):
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'name',
            'image',
            'effect',
            'target',
            'extra_profit',
        ]
