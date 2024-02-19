from app.models import Sector, ProductCard, Trader, Game, Player
from django.core.exceptions import ObjectDoesNotExist


class TraderService:
    @staticmethod
    def hire(player_id, sector_id, products_ids):
        player = Player.objects.get(id=player_id)
        sector = Sector.objects.get(id=sector_id)

        trader = Trader.objects.create(sector=sector)
        trader.products.set(ProductCard.objects.filter(id__in=products_ids))
        trader.save()

        player.traders.add(trader)
        player.save()

        return trader
