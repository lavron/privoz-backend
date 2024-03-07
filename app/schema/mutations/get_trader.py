import graphene

from app.models import Player, Trader, BaseSector, Sector, Product, ProductCard
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

        player = Player.objects.get(id=player_id)
        game = player.game
        base_sector = BaseSector.objects.get(id=sector_id)
        sector = Sector.objects.get(sector=base_sector, game=game)

        if not sector:
            raise Exception(f"Invalid sector id {sector_id}.")

        check = GameRulesChecker(game)
        check.can_player_get_trader(player_id, sector_id, product_cards_ids)

        trader = Trader.create(player_id, sector.id)

        for product_card_id in product_cards_ids:
            base_product_card = Product.objects.get(id=product_card_id)
            print("👉🏻base_product_card", base_product_card)
            product_card = player.product_cards.filter(card=base_product_card, game=game).first()          
            if not product_card:
                raise Exception(f"Invalid product card id {product_card_id}.")
            player.product_cards.remove(product_card)
            trader.product_cards.append(product_card)
        trader.save()
        player.save()
        game.queue.next_turn()
        return GetTrader(trader=trader)
