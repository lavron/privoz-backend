import graphene

from app.models import Player
from app.schema.services.trader_service import TraderService
from app.schema.types.player_type import PlayerType
from app.schema.types.trader_type import TraderType


class HireTrader(graphene.Mutation):
    class Arguments:
        player_id = graphene.Int(required=True)
        sector_id = graphene.Int(required=True)

    # Output = PlayerType

    trader = graphene.Field(lambda: TraderType)

    @staticmethod
    def mutate(root, info, player_id, sector_id):
        player = Player.objects.get(id=player_id)
        game = player.game

        if player_id != game.active_player_id:
            turn_error_message = f"It is not player {player_id}'s turn, it's player {player.game.active_player_id}'s turn."
            raise Exception(turn_error_message)

        if game.current_phase != 'hire_trader':
            phase_error_message = f"It is not the right phase to hire a trader. The current phase is {game.current_phase}."
            raise Exception(phase_error_message)

        trader = TraderService.hire(player_id, sector_id)

        player.game.end_turn()
        return HireTrader(trader=trader)
