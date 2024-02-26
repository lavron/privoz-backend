from typing import List

import strawberry_django

from app.models import EventCard

from app.models import EventCardDeck


@strawberry_django.type(EventCardDeck)
class EventCardDeckType:
    cards: List["app.schema.types.event_card_in_deck.EventCardInDeckType"]
    pass

@strawberry_django.type(EventCard, fields="__all__")
class EventCardType:
    pass
