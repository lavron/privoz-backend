import strawberry_django

from app.models import EventCard


@strawberry_django.type(EventCard, fields="__all__")
class EventCardType:
    pass
