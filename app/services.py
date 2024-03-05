import random

from app.models import Sector, BaseEventCard, EventCard, BaseProductCard, ProductCard, Player
from app.models import Hero
from app.models.sector import BaseSector


class GameResourcesCreator:
    @staticmethod
    def create(game):
        from app.models import GameQueue

        # Trader Capacity
        game.trader_capacity = game.players_count

        # EventCards
        event_cards = BaseEventCard.objects.all()
        for event_card in event_cards:
            EventCard.objects.create(card=event_card, game=game)

        # ProductCards
        product_cards = BaseProductCard.objects.all()
        for product_card in product_cards:
            ProductCard.objects.create(card=product_card, game=game)

        # Sectors
        sectors = BaseSector.objects.all()
        for sector in sectors:
            Sector.objects.create(sector=sector, game=game)

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

        game.queue = GameQueue.objects.create(game=game)
        game.queue.players_order_ids = ids
        game.queue.active_player_id = ids[0]


        game.save()

