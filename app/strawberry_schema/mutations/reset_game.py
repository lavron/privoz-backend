import strawberry
from app.strawberry_schema.services.game_service import GameService
from app.strawberry_schema.types.game_type import GameType


@strawberry.type
class ResetGameOutput:
    game: GameType

@strawberry.input
class ResetGameInput:
    game_id: int = None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def reset_game(self, input: ResetGameInput) -> ResetGameOutput:
        game = GameService.reset(game_id=input.game_id)
        return ResetGameOutput(game=game)