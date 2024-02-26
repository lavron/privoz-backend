import strawberry
from app.models import Game  # change to your actual import path
from app.strawberry_schema.types.game_type import GameType

@strawberry.type
class GameMutation:
    @strawberry.mutation
    def create_game(self, info, title: str) -> GameType:
        # the logic to create a game
        pass