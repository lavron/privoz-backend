import strawberry_django

from app.models import Trader
from typing import List

@strawberry_django.type(Trader)
class TraderType:
    id: int
    sector_id: int
    player_id: int
    price: int = 1
    products: List[int]


