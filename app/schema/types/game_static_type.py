import strawberry_django

from app.models import Game


@strawberry_django.type(Game)
class GameStaticType:
    id: int
    players_count: int
    trader_capacity: int
