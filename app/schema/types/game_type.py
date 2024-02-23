from typing import Optional, List

import strawberry_django
import strawberry

from app.models import Game
from app.schema.types.event_card_deck_type import EventCardDeckType
from app.schema.types.player_type import PlayerType
from app.schema.types.product_card_deck_type import ProductCardDeckType
from app.schema.types.sector_type import SectorType
from asgiref.sync import sync_to_async


@strawberry_django.type(
    Game,
    fields=["id", "players_count",
            "active_player_id", "players_order_ids", "players_order_index",
            "current_phase"])
class GameType:
    product_cards_deck: ProductCardDeckType
    event_cards_deck: EventCardDeckType
    sectors: List[SectorType]
    players: List[PlayerType]
    active_player_id: Optional[int]
    players_order_ids: List[int]

    #
    async def resolve_sectors(self, info) -> List[SectorType]:
        sectors = await sync_to_async(self.sectors.all, thread_sensitive=True)()
        return [SectorType(sector_data) for sector_data in sectors]

    @strawberry.field
    async def resolve_players(self, info) -> List[PlayerType]:
        players = await sync_to_async(self.players.all, thread_sensitive=True)()
        return [PlayerType(player_data) for player_data in players]

    @strawberry.field
    async def resolve_product_cards_deck(self, info) -> ProductCardDeckType:
        product_cards_deck = await sync_to_async(lambda: self.product_cards_deck)()
        return ProductCardDeckType(product_cards_deck)

    @strawberry.field
    async def resolve_event_cards_deck(self, info) -> EventCardDeckType:
        event_cards_deck = await sync_to_async(lambda: self.event_cards_deck)()
        return EventCardDeckType(event_cards_deck)
