import graphene

from app.models import Player
from app.schema.types import TraderForUserType
from app.services.game_engine import GameEngine


class GetTrader(graphene.Mutation):
    class Arguments:
        player_id = graphene.Int(required=True)
        sector_id = graphene.Int(required=True)
        product_cards_ids = graphene.List(graphene.Int)

    trader = graphene.Field(lambda: TraderForUserType)

    @staticmethod
    def mutate(root, info, player_id, sector_id, product_cards_ids):

        player = Player.objects.get(id=player_id)
        game = player.game

        game_engine = GameEngine(game)
        trader = game_engine.create_trader(player_id, sector_id, product_cards_ids)

        return GetTrader(trader=trader)
