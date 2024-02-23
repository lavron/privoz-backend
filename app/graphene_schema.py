import graphene

from app.graphene_schema.mutations.hire_trader import HireTrader
from app.graphene_schema.mutations.reset_game import ResetGame
from app.graphene_schema.types.box_type import BoxType
from app.graphene_schema.types.game_type import GameType
from app.graphene_schema.services.game_service import GameService
from app.graphene_schema.services.box_service import BoxService
from graphene_django.debug import DjangoDebug

import asyncio
from datetime import datetime


class Mutation(graphene.ObjectType):
    hire_trader = HireTrader.Field()
    reset_game = ResetGame.Field()
    debug = graphene.Field(DjangoDebug, name='_debug')


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


class Subscription(graphene.ObjectType):
    time_of_day = graphene.String()

    async def subscribe_time_of_day(root, info):
        while True:
            yield datetime.now().isoformat()
            await asyncio.sleep(1)


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)

