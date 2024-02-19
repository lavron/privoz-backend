from app.models import Sector, ProductCard, Trader, Game
from django.core.exceptions import ObjectDoesNotExist


class TraderService:
    @staticmethod
    def add(game_id, player_id, sector_id, products_ids):
        # try:
        game = Game.objects.get(id=game_id)
        print("👉🏻game.players", game.players)
        print("👉🏻player_id", player_id)
        player = game.players.get(id=player_id)
        print("👉🏻player", player)
        sector = Sector.objects.get(id=sector_id)
        print("👉🏻sector", sector)
        # except ObjectDoesNotExist:
        #     return "Object not found."

        trader = Trader.objects.create(sector=sector)
        trader.products.set(ProductCard.objects.filter(id__in=products_ids))
        trader.save()

        player.traders.add(trader)
        player.save()

        return trader
