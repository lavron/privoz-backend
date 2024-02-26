import strawberry_django

from app.models.event_card import EventCardInDeck
from app.strawberry_schema.types.event_card_deck_type import EventCardDeckType
from app.strawberry_schema.types.event_card_type import EventCardType

@strawberry_django.type(EventCardInDeck)
class EventCardInDeckType:
    card: EventCardType
    deck: EventCardDeckType
    pass
