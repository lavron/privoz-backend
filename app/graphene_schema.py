import graphene
from app.schema.mutations.hire_trader import HireTrader
from app.schema.types.box_type import BoxType
from app.schema.types.game_type import GameType
from app.schema.services.game_service import GameService
from app.schema.services.box_service import BoxService

class Mutation(graphene.ObjectType):
    hire_trader = HireTrader.Field()

class Query(graphene.ObjectType):
    box = graphene.Field(BoxType)
    games = graphene.List(GameType)
    game = graphene.Field(GameType, pk=graphene.ID(required=False))

    def resolve_game(self, info, pk=None, **kwargs):
        return GameService.get_game(pk)

    def resolve_games(self, info, **kwargs):
        return GameService.get_all_games()

    def resolve_box(self, info, **kwargs):
        return BoxService.get_content()


schema = graphene.Schema(query=Query, mutation=Mutation)