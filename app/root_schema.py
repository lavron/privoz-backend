from typing import List

import strawberry

from app.test_schema.queries.game_query import GameQuery, GameType
from privoz.utils import last_game_id


@strawberry.type
class Query(GameQuery):

    @strawberry.field
    def respond(self) -> str:
        return "Hello, World!"

    @strawberry.field
    def games(self, info) -> List[GameType]:
        return GameQuery.games(self, info)

    @strawberry.field
    def game(self, info, game_id: int = None) -> GameType:
        if not game_id:
            game_id = last_game_id()
        return GameQuery.game(self, info, game_id)


schema = strawberry.Schema(query=Query)
