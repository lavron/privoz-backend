import graphene

from app.schema.types.game_type import GameType, BaseGameType
from app.schema.services.game_service import GameService

game_service = GameService()

class GameQuery(graphene.ObjectType):
    game = graphene.Field(GameType, game_id=graphene.Int())
    games = graphene.List(BaseGameType)

    @staticmethod
    def resolve_game(root, info, game_id):
        return game_service.get_game(game_id)

    @staticmethod
    def resolve_games(root, info):
        return game_service.get_all_games()