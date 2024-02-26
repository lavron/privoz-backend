import strawberry_django

from typing import List
from app.models import EventCardDeck


@strawberry_django.type(EventCardDeck)
class EventCardDeckType:
    cards: List["app.schema.types.event_card_in_deck.EventCardInDeckType"]
    pass