import strawberry
import asyncio
from typing import List, Optional

from app.models import Hero, Sector, ProductCard, EventCard
from app.schema.types.event_card_type import EventCardType
from app.schema.types.hero_type import HeroType
from app.schema.types.product_card_deck_type import ProductCardType
from app.schema.types.sector_type import SectorType

from asgiref.sync import sync_to_async


@strawberry.type
class BoxType:
    heroes: Optional[List[HeroType]] = None
    sectors: Optional[List[SectorType]] = None
    product_cards: Optional[List[ProductCardType]] = None
    event_cards: Optional[List[EventCardType]] = None

    @staticmethod
    @strawberry.field
    async def resolve_heroes(root) -> Optional[List[HeroType]]:
        heroes = await sync_to_async(Hero.objects.all, thread_sensitive=True)()
        return [HeroType(hero_data) for hero_data in heroes] if heroes else None

    @staticmethod
    @strawberry.field
    async def resolve_sectors(root) -> Optional[List[SectorType]]:
        sectors = await sync_to_async(Sector.objects.all, thread_sensitive=True)()
        return [SectorType(sector_data) for sector_data in sectors] if sectors else None

    @staticmethod
    @strawberry.field
    async def resolve_product_cards(root) -> Optional[List[ProductCardType]]:
        product_cards = await sync_to_async(ProductCard.objects.all, thread_sensitive=True)()
        return [ProductCardType(card_data) for card_data in product_cards] if product_cards else None

    @staticmethod
    @strawberry.field
    async def resolve_event_cards(root) -> Optional[List[EventCardType]]:
        event_cards = await sync_to_async(EventCard.objects.all, thread_sensitive=True)()
        return [EventCardType(card_data) for card_data in event_cards] if event_cards else None
