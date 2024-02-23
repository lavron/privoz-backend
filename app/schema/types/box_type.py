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

    @strawberry.field
    async def heroes(self, info) -> Optional[List[HeroType]]:
        heroes = await sync_to_async(list)(Hero.objects.all())
        if heroes:
            hero_types = [HeroType(
                id=hero.id,
                name=hero.name,
                color=hero.color,
                image=hero.image,
                premium_sector=hero.premium_sector,
                event_card_protection=hero.event_card_protection
            ) for hero in heroes]
        else:
            return None

    @strawberry.field
    async def sectors(root) -> Optional[List[SectorType]]:
        sectors = await sync_to_async(Sector.objects.all, thread_sensitive=True)()
        return [SectorType(sector_data) for sector_data in sectors] if sectors else None

    @strawberry.field
    async def product_cards(root) -> Optional[List[ProductCardType]]:
        product_cards = await sync_to_async(ProductCard.objects.all, thread_sensitive=True)()
        return [ProductCardType(card_data) for card_data in product_cards] if product_cards else None

    @strawberry.field
    async def event_cards(root) -> Optional[List[EventCardType]]:
        event_cards = await sync_to_async(EventCard.objects.all, thread_sensitive=True)()
        return [EventCardType(card_data) for card_data in event_cards] if event_cards else None