import graphene

from app.schema.mutations import GetTrader
from app.schema.types.game_type import GameType
from app.schema.services.game_service import GameService
from graphene_django.debug import DjangoDebug

import logging

logger = logging.getLogger(__name__)


class Mutation(graphene.ObjectType):
    get_trader = GetTrader.Field()
    debug = graphene.Field(DjangoDebug, name='_debug')


class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    game = graphene.Field(GameType, pk=graphene.ID(required=False))
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_game(self, info, pk=None, **kwargs):
        try:
            game = GameService.get_game(pk)
            return game
        except Exception as e:
            logger.exception('Error resolving Your Query Name')
            raise e

    def resolve_games(self, info, **kwargs):
        return GameService.get_all_games()


schema = graphene.Schema(query=Query, mutation=Mutation)
