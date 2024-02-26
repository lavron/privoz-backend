import strawberry
from app.models import Player
from app.strawberry_schema.services.trader_service import TraderService
from app.strawberry_schema.types.player_type import PlayerType
from app.strawberry_schema.types.trader_type import TraderType


@strawberry.type
class HireTraderOutput:
    trader: TraderType


@strawberry.input
class HireTraderInput:
    player_id: int
    sector_id: int


@strawberry.type
class Mutation:
    @strawberry.mutation
    def hire_trader(self, input: HireTraderInput) -> HireTraderOutput:
        player = Player.objects.get(id=input.player_id)
        game = player.game

        if input.player_id != game.active_player_id:
            turn_error_message = f"It is not player {input.player_id}'s turn, it's player {input.game.active_player_id}'s turn."
            raise Exception(turn_error_message)

        if game.current_phase != 'hire_trader':
            phase_error_message = f"It is not the right phase to hire a trader. The current phase is {input.game.current_phase}."
            raise Exception(phase_error_message)

        trader = TraderService.hire(input.player_id, input.sector_id)

        player.game.end_turn()
        return HireTraderOutput(trader=trader)