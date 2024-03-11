import graphene

from app.models import Player, Trader, Sector, ProductCard
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

        player = Player.objects.get(id=player_id)
        game = player.game
        sector = Sector.objects.get(id=sector_id)

        if not sector:
            raise Exception(f"Invalid sector id {sector_id}.")

        check = GameRulesChecker(game)
        check.can_player_get_trader(player_id, sector_id, product_cards_ids)

        trader = Trader.create(player, sector)

        for id in product_cards_ids:
            product_card = ProductCard.objects.get(id=id)
            player.product_cards.remove(product_card)
            trader.product_cards.append(product_card)

        trader.save()
        player.save()
        game.queue.next_turn()
        return GetTrader(trader=trader)
