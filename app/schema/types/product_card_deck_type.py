import strawberry_django
from app.models import ProductCardDeck, ProductCardInDeck, ProductCard
from app.schema.types.sector_type import SectorType
from typing import List

@strawberry_django.type(ProductCard)
class ProductCardType:
    sector: SectorType

@strawberry_django.type(ProductCardInDeck)
class ProductCardInDeckType:
    card: ProductCardType
    deck: 'ProductCardDeckType'

@strawberry_django.type(ProductCardDeck)
class ProductCardDeckType:
    cards: List[ProductCardInDeckType]