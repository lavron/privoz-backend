from typing import List

import strawberry
import strawberry_django
from strawberry import auto

from app.models import Game

@strawberry_django.type(Game, fields=["active_player_id", "current_phase"])
class GameMoveOrderType:
    active_player_id: int
    players_order_ids: List[int]
    current_phase: str