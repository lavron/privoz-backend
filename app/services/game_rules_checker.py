from app.models import Sector, ProductCard, BaseSector, Product


class GameRulesChecker:
    def __init__(self, game):
        self.game = game

    def can_player_get_trader(self, player_id, sector_id, product_cards_ids):
        check = self
        check.phase('GET_TRADER')
        check.player_turn(player_id)
        check.player_can_buy(player_id, product_cards_ids)
        check.sector_spots_available(sector_id)
        check.sector_for_products(sector_id, product_cards_ids)

    def phase(self, current_phase):
        if current_phase != self.game.queue.phase:
            raise Exception(f"Invalid phase. The current phase is {self.game.queue.phase}.")

    def player_turn(self, player_id):
        active_player_id = self.game.queue.active_player_id
        if player_id != active_player_id:
            raise Exception(
                f"It is not player {player_id}'s turn, it's player {self.game.queue.active_player_id}'s turn.")

    def player_can_buy(self, player_id, product_cards_ids):
        sum_coins = 0
        player_coins = self.game.players.get(id=player_id).coins

        for card_id in product_cards_ids:
            product_card = ProductCard.objects.get(id=card_id)
            buy_price = product_card.product.buy_price
            sum_coins += buy_price
            if sum_coins > player_coins:
                raise Exception(
                    f"Player {self.game.queue.active_player_id} does not have enough coins to buy the card.")

    def sector_spots_available(self, sector_id):
        sector = Sector.objects.get(id=sector_id)
        if sector.traders.count() >= self.game.trader_capacity:
            raise Exception(f"Trader capacity for sector {sector_id} is full.")

    def sector_for_products(self, sector_id, product_cards_ids):
        for product_card_id in product_cards_ids:
            product_card = ProductCard.objects.get(id=product_card_id)
            if product_card.sector.id != sector_id:
                raise Exception(
                    f"Product card {product_card_id} ({product_card.product.name}) does not belong to sector {sector_id} ({sector.name}).")
