from django.db import transaction
from django.db.models import Prefetch

from app.game_config import DRAW_PRODUCT_CARDS_COUNT, TRADER_SALARY
from app.models import ProductCard, Trader, Player, Sector
from app.services import GameResourcesCreator, GameRulesChecker
from abc import ABC, abstractmethod



class PhaseCommand(ABC):
    @abstractmethod
    def execute(self, game_engine):
        pass


class DrawProductCardsCommand(PhaseCommand):
    def execute(self, game_engine):
        from app.schema.subscriptions.subscription import update_player

        cards_to_assign = game_engine.draw_top_cards(DRAW_PRODUCT_CARDS_COUNT)
        active_player = game_engine.game.active_player

        game_engine.assign_cards_to_player(active_player, cards_to_assign)
        game_engine.game.active_player.save()

        update_player(active_player)

        game_engine.game.queue.next_turn()


class GetTraderCommand(PhaseCommand):
    def execute(self, game_engine):
        # Your implementation for GET_TRADER phase
        pass


class MakeSalesCommand(PhaseCommand):
    def execute(self, game_engine):
        from app.schema.subscriptions.subscription import update_player
        
        print("👉🏻MakeSalesCommand")

        active_player = game_engine.game.active_player

        for trader in active_player.traders.all():
            for product_card in trader.product_cards.all():
                active_player.coins += product_card.product.sell_price
        active_player.save()
        update_player(active_player)
        game_engine.game.queue.next_turn()


class PaycheckCommand(PhaseCommand):
    def execute(self, game_engine):
        from app.schema.subscriptions.subscription import update_player
        active_player = game_engine.game.active_player
        for trader in active_player.traders.all():
            active_player.coins -= TRADER_SALARY
        active_player.save()
        update_player(active_player)


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
        self.check = GameRulesChecker(self.game)

    def create_trader(self, player_id, sector_id, product_cards_ids):

        from app.schema.subscriptions.subscription import update_player, update_sector

        self.check.can_player_get_trader(player_id, sector_id, product_cards_ids)

        sector = Sector.objects.get(id=sector_id)
        trader = Trader.create(player_id=player_id, sector_id=sector_id)
        player = Player.objects.get(id=player_id)

        product_cards = ProductCard.objects.filter(id__in=product_cards_ids)
        amount = 0
        for product_card in product_cards:
            product_card.player = None
            product_card.save()
            amount += product_card.product.buy_price
            trader.product_cards.add(product_card)

        trader.save()
        sector.traders.add(trader)
        sector.save()
        self.charge_player(player, amount)

        update_player(player_id)
        update_sector(sector_id)

        self.game.queue.next_turn()

        return trader

    def charge_player(self, player, amount):
        player.coins -= amount
        player.save()

    def handle_phase(self):
        print("👉🏻handle_phase",self.game.queue.phase )
        func = self.phase_dispatch.get(self.game.queue.phase)
        if func:
            print("👉🏻func, func")
            func.execute(self)
        else:
            print(f"Unknown phase: {self.game.current_phase}")

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

