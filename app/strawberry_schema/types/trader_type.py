import strawberry_django


from app.models import Trader
from typing import List

from app.strawberry_schema.types.player_type import PlayerType

@strawberry_django.type(Trader)
class TraderType:
    sector: "SectorType"
    products: List["ProductCardInDeckType"]
    player: PlayerType
