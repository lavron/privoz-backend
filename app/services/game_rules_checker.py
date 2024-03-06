from app.models import Sector, ProductCard, BaseSector, Product


class GameRulesChecker:
    def __init__(self, game):
        self.game = game

    def can_player_get_trader(self, player_id, sector_id, product_cards_ids):
        self.check_current_phase('GET_TRADER')
        self.check_player_turn(player_id)
        self.check_free_spots(sector_id)
        for product_card_id in product_cards_ids:
            self.can_player_place_product_card(sector_id, product_card_id)

    def can_player_place_product_card(self, sector_id, product_card_id):
        base_product_card = Product.objects.get(id=product_card_id)
        base_sector = BaseSector.objects.get(id=sector_id)
        if base_product_card.sector != base_sector:
            raise Exception(f"Product card {product_card_id} ({base_product_card.name}) does not belong to sector {sector_id} ({base_sector.name}).")
        print("👉🏻can_player_place_product_card ok!")

    def check_player_can_buy(self, product_cards_ids):
        total = 0
        player_coins = self.game.players.get(id=self.game.queue.active_player_id).coins

        for card_id in product_cards_ids:
            base_card = self.game.product_cards.filter(id=card_id).first()
            total += base_card.buy_price
            if total > player_coins:
                raise Exception(
                    f"Player {self.game.queue.active_player_id} does not have enough coins to buy the card.")
        print("👉🏻check_player_can_buy ok!")

    def check_free_spots(self, sector_id):
        base_sector = BaseSector.objects.get(id=sector_id)
        sector = Sector.objects.get(sector=base_sector, game=self.game)
        if sector.traders.count() >= self.game.trader_capacity:
            raise Exception(f"Trader capacity for sector {sector_id} is full.")
        print("👉🏻check_free_spots ok!")

    def check_current_phase(self, current_phase):
        if current_phase != self.game.queue.phase:
            raise Exception(f"Invalid phase. The current phase is {self.game.queue.phase}.")

    def check_player_turn(self, player_id):
        print("👉🏻player_id", player_id)
        print("👉🏻self.game.queue.active_player_id", self.game.queue.active_player_id)
        if player_id != self.game.queue.active_player_id:
            return Exception(
                f"It is not player {player_id}'s turn, it's player {self.game.queue.active_player_id}'s turn.")
        print("👉🏻check_player_turn ok!")
