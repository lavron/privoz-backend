from app.models import Sector, ProductCard, Trader, Game, Player
from django.core.exceptions import ObjectDoesNotExist


class TraderService:
    @staticmethod
    def get(player_id, sector_id, product_cards_ids):
        player = Player.objects.get(id=player_id)
        sector = Sector.objects.get(id=sector_id)
        product_cards = ProductCard.objects.filter(id__in=product_cards_ids)

        trader = Trader.objects.create(sector=sector)
        trader.save()

        for card_id in product_cards_ids:
            card = ProductCard.objects.get(id=card_id)
            trader.product_cards.add(card)
            trader.save()

        player.traders.add(trader)
        player.save()

        return trader
