import graphene

from app.models import Player, Trader
from app.schema.services.trader_service import TraderService
from app.schema.types import TraderForUserType
from app.services.game_rules_checker import GameRulesChecker


class GetTrader(graphene.Mutation):
    class Arguments:
        player_id = graphene.Int(required=True)
        sector_id = graphene.Int(required=True)
        product_cards_ids = graphene.List(graphene.Int)

    trader = graphene.Field(lambda: TraderForUserType)

    @staticmethod
    def mutate(root, info, player_id, sector_id, product_cards_ids):
        import logging
        logger = logging.getLogger(__name__)

        player = Player.objects.get(id=player_id)
        game = player.game

        check = GameRulesChecker(game)

        try:
            check.can_player_get_trader(player_id, sector_id, product_cards_ids)
        except Exception as e:
            logger.exception('checking rules')
            raise e


        trader = Trader.create(player_id, sector_id, product_cards_ids)

        game.queue.end_turn()
        return GetTrader(trader=trader)
