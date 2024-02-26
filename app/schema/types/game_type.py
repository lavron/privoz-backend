import strawberry
import strawberry_django
from app.models import Game
from typing import List

from app.schema.types.game_move_order_type import GameMoveOrderType
# from app.schema.types.game_move_order_type import GameMoveOrderType
from app.schema.types.game_static_type import GameStaticType
from app.schema.types.player_type import PlayerType
from app.schema.types.sector_type import SectorType


@strawberry_django.type(Game)
class GameType:
    move_order: GameMoveOrderType
    players: List[PlayerType]
    sectors: List[SectorType]

    # product_cards_deck: ProductCardDeckType
    # event_cards_deck: EventCardDeckType

    @strawberry.field
    def static_info(self, info) -> GameStaticType:
        return GameStaticType(
            id=self.id,
            players_count=self.players_count,
            trader_capacity=self.trader_capacity)

    @strawberry.field
    def move_order(self, info) -> GameMoveOrderType:
        return GameMoveOrderType(
            players_order_ids=self.players_order_ids,
            # players_order_index=self.players_order_index,
            active_player_id=self.active_player_id,
            current_phase=self.current_phase)


# write a class to hold the order of players_order_ids, active_player_id, and current_phase

# write a class to hold the order of players_order_ids, active_player_id, and current_phase
@strawberry_django.type(Game)
class GameOrderType:
    players_order_ids: List[int]
    active_player_id: int
    current_phase: int
    pass
