from typing import List

import strawberry
import strawberry_django

from app.models import Game

from asgiref.sync import sync_to_async

from app.schema.types.game_type import GameType


@strawberry.type
class GameQuery:
    @strawberry.field
    async def games(self, info) -> List[GameType]:
        games = await sync_to_async(lambda: list(Game.objects.all()), thread_sensitive=True)()
        return games

    @strawberry.field
    async def game(self, info, game_id: int = None) -> GameType:
        if not game_id:
            game_id = await last_game_id()
        game = await sync_to_async(Game.objects.get, thread_sensitive=True)(id=game_id)
        return game

async def last_game_id():
    game_ids = Game.objects.order_by('-id').values_list('id', flat=True)
    last_id = await sync_to_async(game_ids.first, thread_sensitive=True)()
    return last_id