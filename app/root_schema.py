from typing import List

import strawberry

from app.schema.queries.game_query import GameQuery, GameType
from privoz.utils import last_game_id


@strawberry.type
class Query(GameQuery):

    @strawberry.field
    async def games(self, info) -> List[GameType]:
        return await GameQuery.games(self, info)

    @strawberry.field
    async def game(self, info, game_id: int = None) -> GameType:
        return await GameQuery.game(self, info, game_id)


schema = strawberry.Schema(query=Query)
