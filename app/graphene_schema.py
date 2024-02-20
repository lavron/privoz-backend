
import graphene

from app.schema.mutations.hire_trader import HireTrader
from app.schema.mutations.reset_game import ResetGame
from app.schema.types.box_type import BoxType
from app.schema.types.game_type import GameType
from app.schema.services.game_service import GameService
from app.schema.services.box_service import BoxService
from graphene_django.debug import DjangoDebug
from graphene import ObjectType

from app.schema.types.player_type import PlayerType


class Mutation(graphene.ObjectType):
    hire_trader = HireTrader.Field()
    reset_game = ResetGame.Field()
    debug = graphene.Field(DjangoDebug, name='_debug')


class Subscription(ObjectType):
    player_updated = graphene.Field(PlayerType)
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_player_updated(root, info):
        return player_updated.pipe(ops.map(lambda x: PlayerType(player=x)))

class Query(graphene.ObjectType):
    box = graphene.Field(BoxType)
    games = graphene.List(GameType)
    game = graphene.Field(GameType, pk=graphene.ID(required=False))
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_game(self, info, pk=None, **kwargs):
        return GameService.get_game(pk)

    def resolve_games(self, info, **kwargs):
        return GameService.get_all_games()

    def resolve_box(self, info, **kwargs):
        return BoxService.get_content()


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
