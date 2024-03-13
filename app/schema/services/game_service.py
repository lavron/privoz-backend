from app.models import Game


def last_game_id():
    return Game.objects.order_by('-id').values_list('id', flat=True).first()


class GameService:

    @staticmethod
    def get_game(game_id=None):
        game_id = game_id if game_id else last_game_id()
        try:
            return Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return None

    @staticmethod
    def get_all_games():
        return Game.objects.all()

    @staticmethod
    def create_game(players_count=2):
        game = Game.objects.create(players_count=players_count)
        game.save()
        return game

