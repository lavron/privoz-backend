import graphene

from app.graphene_schema.services.trader_service import TraderService
from app.graphene_schema.types.trader_type import TraderType


class AddTrader(graphene.Mutation):
    class Arguments:
        game_id = graphene.Int(required=True)
        player_id = graphene.Int(required=True)
        sector_id = graphene.Int(required=True)
        products_ids = graphene.List(graphene.Int, required=True)

    trader = graphene.Field(lambda: TraderType)

    @staticmethod
    def mutate(root, info, game_id, player_id, sector_id, products_ids):
        trader = TraderService.add(game_id, player_id, sector_id, products_ids)
        return AddTrader(trader=trader)