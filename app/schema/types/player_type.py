import strawberry_django
from typing import Optional, List

from app.models import Player
from app.schema.types.event_card_in_deck import EventCardInDeckType
from app.schema.types.hero_type import HeroType

@strawberry_django.type(Player)
class PlayerType:
    hero: HeroType
    game: "GameType"
    event_cards: List[EventCardInDeckType]
    traders: Optional[List["TraderType"]]