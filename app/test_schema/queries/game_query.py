from typing import List

import asyncio

import strawberry
import strawberry_django

from app.models import Game

from asgiref.sync import sync_to_async


@strawberry_django.type(
    Game,
    fields=["id", "players_count",
            "active_player_id", "players_order_ids", "players_order_index",
            "current_phase"])
class GameType:
    players_order_ids: List[int]
    pass


@strawberry.type
class GameQuery:
    @strawberry.field
    async def games(self, info) -> List[GameType]:
        games = await sync_to_async(lambda: list(Game.objects.all()), thread_sensitive=True)()
        return games

    @strawberry.field
    async def game(self, info, id: int) -> GameType:
        game = await sync_to_async(Game.objects.get, thread_sensitive=True)(id=id)
        return game
