from typing import List
import graphene

from app.schema.services.game_service import last_game_id
from app.schema.types import TraderForUserType
from app.services.game_engine import GameEngine


class GetTrader(graphene.Mutation):
    class Arguments:
        player_id = graphene.Int()
        sector_id = graphene.Int()
        product_cards_ids = graphene.List(graphene.Int)

    trader = graphene.Field(lambda: TraderForUserType)

    @staticmethod
    def mutate(root, info, player_id=None, sector_id=None, product_cards_ids=None):
        from app.models import Player, Game
        
        if not player_id:
            game_id = last_game_id()
            game = Game.objects.get(id=game_id)
            player_id = game.queue.active_player_id
            
        player = Player.objects.get(id=player_id)
        game = player.game
        
        product_cards = player.product_card.all()
        first_product_card = product_cards.first()
        if not sector_id:
            sector_id = first_product_card.sector.id
        if not product_cards_ids:
            product_cards_ids =[first_product_card.id]



        game_engine = GameEngine(game)
        trader = game_engine.create_trader(player_id, sector_id, product_cards_ids)

        return GetTrader(trader=trader)
