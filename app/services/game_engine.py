from django.db import transaction
from django.db.models import Prefetch, Sum, F

from app.game_config import DRAW_PRODUCT_CARDS_COUNT, TRADER_SALARY
from app.models import ProductCard, Trader, Player
from app.services import GameResourcesCreator
from abc import ABC, abstractmethod


class PhaseCommand(ABC):
    @abstractmethod
    def execute(self, game_engine):
        pass


class DrawProductCardsCommand(PhaseCommand):
    def execute(self, game_engine):
        cards_to_assign = game_engine.draw_top_cards(DRAW_PRODUCT_CARDS_COUNT)
        with transaction.atomic():
            game_engine.assign_cards_to_player(game_engine.game.active_player, cards_to_assign)
            for player in game_engine.players:
                player.save()
        game_engine.game.queue.next_turn()


class GetTraderCommand(PhaseCommand):
    def execute(self, game_engine):
        # Your implementation for GET_TRADER phase
        pass


class MakeSalesCommand(PhaseCommand):
    def execute(self, game_engine):
        # Your implementation for SALES phase
        pass


class PaycheckCommand(PhaseCommand):
    def execute(self, game_engine):
        # Your implementation for PAYCHECK phase
        pass


class GameEngine:
    def __init__(self, game):
        self.game = game
        self.players = self.game.players.all().prefetch_related(
            Prefetch('traders', queryset=Trader.objects.all().prefetch_related('product_cards')))
        self.shuffle = GameResourcesCreator.shuffle_cards
        self.phase_dispatch = {
            "DRAW_PRODUCT_CARDS": DrawProductCardsCommand(),
            "GET_TRADER": GetTraderCommand(),
            "SALES": MakeSalesCommand(),
            "PAYCHECK": PaycheckCommand(),
        }

    def handle_phase(self):
        func = self.phase_dispatch.get(self.game.queue.phase)
        if func:
            func.execute(self)
        else:
            print(f"Unknown phase: {self.game.current_phase}")


    def phase_get_trader(self):
        print("👉🏻GameEngine.get_trader() mutation")
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
        self.game.queue.next_phase()

    def phase_paycheck(self):
        print("👉🏻GameEngine.paycheck()")
        for player in self.players:
            for _ in player.traders.all():
                player.coins -= TRADER_SALARY
            player.save()
        self.game.queue.next_phase()

    def phase_draw_product_cards(self):
        cards_to_assign = self.draw_top_cards(DRAW_PRODUCT_CARDS_COUNT)
        with transaction.atomic():
            self.assign_cards_to_player(self.game.active_player, cards_to_assign)
            for player in self.players:
                player.save()
        self.game.queue.next_turn()

    def draw_top_cards(self, count):
        cards = self.get_active_product_cards()[:count]
        if len(cards) < count:
            self.shuffle(cards)
            cards = self.get_active_product_cards()[:count]
        self.discard_cards(cards)
        return cards

    def get_active_product_cards(self):
        return ProductCard.objects.filter(game=self.game, is_discarded=False).order_by('-order')

    def discard_cards(self, cards):
        for card in cards:
            card.is_discarded = True
            card.save()

    def assign_cards_to_player(self, player, cards_to_assign):
        for card in cards_to_assign:
            card.player = player
            card.save()


class BaseToInGameConverter:

    @staticmethod
    def convert(game):
        game_engine = GameEngine(game)
        game_engine.handle_phase()
        game.save()
        return game
