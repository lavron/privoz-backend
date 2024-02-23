import strawberry_django

from app.models.event_card import EventCardInDeck
from app.schema.types.event_card_deck_type import EventCardDeckType
from app.schema.types.event_card_type import EventCardType

@strawberry_django.type(EventCardInDeck)
class EventCardInDeckType:
    card: EventCardType
    deck: EventCardDeckType
    pass
