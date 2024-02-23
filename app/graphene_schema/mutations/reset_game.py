import graphene

from app.graphene_schema.services.game_service import GameService
from app.graphene_schema.types.game_type import GameType


class ResetGame(graphene.Mutation):
    game = graphene.Field(lambda: GameType)
    class Arguments:
        game_id = graphene.Int(required=False, default_value=None)

    @staticmethod
    def mutate(root, info, game_id=None):
        game = GameService.reset(game_id=game_id)
        return ResetGame(game=game)
