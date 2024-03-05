from graphene_django import DjangoObjectType
from app.models import EventCard

class EventCardType(DjangoObjectType):
    class Meta:
        model = EventCard

