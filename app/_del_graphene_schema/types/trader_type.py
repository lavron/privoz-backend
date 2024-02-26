import strawberry
from strawberry.django import auto
from typing import List, Optional
from app.models import Trader, Sector, ProductCard, Player  # replace with your exact import paths
from app.strawberry_schema.types.product_card_type import ProductCardType
from app.strawberry_schema.types.sector_type import SectorType


@strawberry.django.type(Trader, fields=auto())
class TraderType:
    sector: SectorType
    products: List[ProductCardType]
    player: Optional[PlayerType]