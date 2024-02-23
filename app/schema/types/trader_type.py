import strawberry_django


from app.models import Trader
from typing import List

from app.schema.types.player_type import PlayerType
from app.schema.types.sector_type import SectorType

@strawberry_django.type(Trader)
class TraderType:
    sector: SectorType
    products: List["ProductCardInDeckType"]
    player: PlayerType
