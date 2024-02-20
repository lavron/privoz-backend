from app.models import Game


def last_game_id():
    print("👉🏻last_game_id")
    return Game.objects.order_by('-id').values_list('id', flat=True).first()


class GameService:

    @classmethod
    def reset(cls, game_id):
        print("👉🏻game_id", game_id)
        game = cls.get_game(game_id)
        print("👉🏻game", game)
        game.reset()
        return game

    @staticmethod
    def get_game(game_id=None):
        print("👉🏻get_game")
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

    def shuffle_product_cards_deck(self, game_id=None):
        game = self.get_game(game_id)
        game.product_cards_deck.shuffle()
        game.product_cards_deck.save()
        return game.product_cards_deck

    def shuffle_event_cards_deck(self, game_id=None):
        game = self.get_game(game_id)
        game.event_cards_deck.shuffle()
        game.event_cards_deck.save()
        return game.event_cards_deck
