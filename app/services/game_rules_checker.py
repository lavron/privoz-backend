class GameRulesChecker:
    def __init__(self, game):
        self.game = game

    def can_player_get_trader(self, player_id, sector_id, product_cards_ids):
        self.check_current_phase('GET_TRADER')
        self.check_player_turn(player_id)
        self.check_free_spots(sector_id)
        self.check_player_can_buy(product_cards_ids)

    def check_player_can_buy(self, product_cards_ids):
        total = 0
        player_coins = self.game.players.get(id=self.game.queue.active_player_id).coins

        for card_id in product_cards_ids:
            base_card = self.game.product_cards.filter(id=card_id).first()
            total += base_card.buy_price
            if total > player_coins:
                raise Exception(
                    f"Player {self.game.queue.active_player_id} does not have enough coins to buy the card.")

    def check_free_spots(self, sector_id):
        if self.game.sector.get(sector__id=sector_id).traders.count() >= self.game.trader_capacity:
            raise Exception(f"Trader capacity for sector {sector_id} is full.")

    def check_current_phase(self, current_phase):
        if current_phase != self.game.queue.phase:
            raise Exception(f"Invalid phase. The current phase is {self.game.queue.current_phase}.")

    def check_player_turn(self, player_id):
        if player_id != self.game.queue.active_player_id:
            return Exception(
                f"It is not player {player_id}'s turn, it's player {self.game.queue.active_player_id}'s turn.")
