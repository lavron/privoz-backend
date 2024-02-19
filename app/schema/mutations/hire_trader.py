import graphene

from app.models import Player
from app.schema.services.trader_service import TraderService
from app.schema.types.trader_type import TraderType


class HireTrader(graphene.Mutation):
    class Arguments:
        player_id = graphene.Int(required=True)
        sector_id = graphene.Int(required=True)
        products_ids = graphene.List(graphene.Int, required=True)

    trader = graphene.Field(lambda: TraderType)

    @staticmethod
    def mutate(root, info, player_id, sector_id, products_ids):
        player = Player.objects.get(id=player_id)

        game = player.game
        current_player_id = game.turn_order[game.current_turn_index]
        if player.id != current_player_id:
            raise Exception('It is not this player\'s turn')

        trader = TraderService.hire(player_id, sector_id, products_ids)
        player.game.end_turn()
        return HireTrader(trader=trader)