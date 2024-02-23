from typing import List

import strawberry

from app.models import Game
from app.schema.types.game_type import GameType


def last_game_id():
    return Game.objects.order_by('-id').values_list('id', flat=True).first()


@strawberry.type
class GameQuery:
    @strawberry.field
    def game(self, info, game_id: int) -> GameType:
        game_id = game_id if game_id else last_game_id()
        try:
            return Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            raise ValueError(f'Game with id {game_id} does not exist')

    @strawberry.field
    def games(self, info) -> List[GameType]:
        return Game.objects.all()