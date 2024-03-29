import random

from django.db import transaction

from app.models import Sector, Product, ProductCard, Player
from app.models import Hero
from app.models.sector import BaseSector


class GameResourcesCreator:

    @staticmethod
    @transaction.atomic
    def shuffle_cards(cards_qs):
        cards = list(cards_qs)
        random.shuffle(cards)
        for i, card in enumerate(cards):
            card.order = i
            card.save()

    @staticmethod
    def create(game):
        from app.models import GameQueue

        # Trader Capacity
        game.trader_capacity = game.players_count

        # Sectors and ProductCards
        base_sectors = BaseSector.objects.all()
        product_cards = []
        for base_sector in base_sectors:
            sector = Sector.objects.create(sector=base_sector, game=game)
            base_sector_products = Product.objects.filter(sector=base_sector)
            for product in base_sector_products:
                for _ in range(product.quantity_in_deck):
                    product_card = ProductCard(product=product, game=game, sector=sector)
                    product_cards.append(product_card)
        product_cards = ProductCard.objects.bulk_create(product_cards)
        GameResourcesCreator.shuffle_cards(product_cards)

        # Players
        heroes = list(Hero.objects.all())
        random.shuffle(heroes)
        heroes = heroes[:game.players_count]

        ids = []
        for hero in heroes:
            player = Player(hero=hero, game=game)
            player.save()
            ids.append(player.pk)
        random.shuffle(ids)

        game.queue = GameQueue.objects.create(game=game, players_order_ids=ids)
        game.queue.reset()

    @staticmethod
    def reset_game(self):
        self.game.queue.reset()
        self.game.queue.players_order_index = 0
        self.game.queue.active_player_id = self.game.queue.players_order_ids[0]
        self.game.queue.save()
        self.game.save()
        self.create(self.game)
        self.game.save()
        self.game.queue.init
