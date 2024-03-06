from django.db import transaction
from django.db.models import Prefetch, Sum, F

from app.game_config import DRAW_PRODUCT_CARDS_COUNT, TRADER_SALARY
from app.models import ProductCard, Trader, Player
from app.services import GameRulesChecker


class GameEngine:
    def __init__(self, game):
        self.game = game
        self.players = self.game.players.all().prefetch_related(
            Prefetch('traders', queryset=Trader.objects.all().prefetch_related('product_cards')))

    def handle_phase(self):
        phase_dispatch = {
            "DRAW_PRODUCT_CARDS": self.phase_draw_product_cards,
            "GET_TRADER": self.phase_get_trader,
            "SALES": self.phase_make_sales,
            "PAYCHECK": self.phase_paycheck,
        }

        func = phase_dispatch.get(self.game.queue.phase)
        if func:
            func()
        else:
            print(f"Unknown phase: {self.game.current_phase}")

    def phase_draw_product_cards(self):
        print("👉🏻GameEngine.distribute_product_cards()")
        cards_to_assign = self.get_product_cards_for_player()

        with transaction.atomic():
            self.assign_cards_to_players(self.players, cards_to_assign)
            for player in self.players:
                player.save()
        self.game.queue.move_to_next_phase()

    def phase_get_trader(self):
        print("👉🏻GameEngine.get_trader()")
        pass


    def phase_make_sales(self):
        print("👉🏻GameEngine.make_sales()")

        all_players = self.game.players.all().prefetch_related(
            Prefetch('traders', queryset=Trader.objects.all().prefetch_related('product_cards')))

        for player in all_players:
            product_cards_qs = ProductCard.objects.filter(trader__player=player)
            player.coins = F('coins') + product_cards_qs.aggregate(total_sell_price=Sum('sell_price'))[
                'total_sell_price']

            for trader in player.traders.all():
                trader.product_cards.clear()

            player.save()
        self.game.queue.move_to_next_phase()

    def phase_paycheck(self):
        print("👉🏻GameEngine.paycheck()")
        for player in self.players:
            for _ in player.traders.all():
                player.coins -= TRADER_SALARY
            player.save()
        self.game.queue.move_to_next_phase()

    def get_product_cards_for_player(self):
        cards = self.game.product_cards.all()[:DRAW_PRODUCT_CARDS_COUNT]
        for card in cards:
            card.is_discarded = True
            card.save()
        return cards

    def assign_cards_to_players(self, players, cards_to_assign):
        for player in players:
            player.product_cards.add(*cards_to_assign)

    def end_game(self):
        # Logic for ending the game and making final calculations
        pass


class BaseToInGameConverter:

    @staticmethod
    def convert(game):
        game_engine = GameEngine(game)
        game_engine.handle_phase()
        game.save()
        return game
