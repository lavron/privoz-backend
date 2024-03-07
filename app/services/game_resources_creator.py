import random

from django.db import transaction

from app.game_config import PHASE_CHOICES
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

        # Products
        products = Product.objects.all()
        for product in products:
            for _ in range(product.quantity_in_deck):
                ProductCard.objects.create(product=product, game=game)
        products = ProductCard.objects.filter(game=game)
        GameResourcesCreator.shuffle_cards(products)

        # Sectors
        base_sectors = BaseSector.objects.all()
        for base_sector in base_sectors:
            Sector.objects.create(sector=base_sector, game=game)
        sectors = Sector.objects.filter(game=game)
        for sector in sectors:
            print(sector.__dict__)

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

        game.queue = GameQueue.objects.create(game=game, phase=PHASE_CHOICES[0][0])
        game.queue.players_order_ids = ids
        game.queue.active_player_id = ids[0]
        game.queue.save()
        game.save()
