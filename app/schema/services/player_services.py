from app.models import Player, Game


class PlayerService:

    def take_event_card(self, game_id, player_id):
        game = Game.objects.get(id=game_id)
        player = Player.objects.get(id=player_id)

        event_card = game.event_cards_deck.draw_card()
        player.event_cards.add(event_card)
        player.save()
        return event_card
