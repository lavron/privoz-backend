from django.http import JsonResponse
from app.models import Game, Player, Sector, ProductCard, EventCard


def game_box(request, game_id):
    game = Game.objects.get(pk=game_id)
    players = Player.objects.filter(games=game)
    sectors = Sector.objects.filter(games=game)
    product_cards = ProductCard.objects.filter(games=game)
    event_cards = EventCard.objects.filter(games=game)

    game_data = {
        'pk': game.pk,
    }
    players_data = [{
        'pk': player.pk,
        'name': player.name,
        'coins': player.coins,
        'color': player.color,
        'premium_sector': player.premium_sector.pk,
        'event_card_protection': player.event_card_protection.pk
    } for player in players]

    sectors_data = [{
        'pk': sector.pk,
        'name': sector.name,
        'description': sector.description} for sector in sectors]

    product_cards_data = [{
        'pk': card.pk,
        'name': card.name,
        'description': card.description,
        'quantity': card.quantity,
        'image': card.image,
        'is_legal': card.is_legal,
        'sector': card.sector.pk,
        'sell_price': card.sell_price,
        'buy_price': card.buy_price,
    } for card in product_cards]

    event_cards_data = [{
        'pk': card.pk,
        'name': card.name,
        'description': card.description,
        'location': card.location,
        'quantity': card.quantity,
        'fortune': card.fortune,
        'target': card.target,
        'confiscation': card.confiscation,
        'protection': card.protection,
        'player_extra_profit': card.player_extra_profit,
        'trader_extra_profit': card.trader_extra_profit,
        'product_extra_profit': card.product_extra_profit,
        'product_extra_item': card.product_extra_item,

        # 'trader_is_active': card.trader_is_active,

    } for card in event_cards]

    data = {
        'game': game_data,
        'players': players_data,
        'sectors': sectors_data,
        'product_cards': product_cards_data,
        'event_cards': event_cards_data,
    }

    return JsonResponse(data, safe=False)
