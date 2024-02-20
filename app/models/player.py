from django.db import models

from .hero import Hero


class Player(models.Model):
    hero = models.ForeignKey(Hero, related_name='players', on_delete=models.CASCADE, null=True)
    game = models.ForeignKey('Game', related_name='players', on_delete=models.CASCADE, null=True)

    event_cards = models.ManyToManyField('EventCardInDeck', through='PlayerEventCard',
                                         related_name='player_cards_in_deck')
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.hero.name

    def reset(self):
        self.coins = 0
        self.traders.clear()
        self.event_cards.clear()
        self.save()


class PlayerEventCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_event_cards')
    event_card = models.ForeignKey('EventCardInDeck', on_delete=models.CASCADE)


class PlayerProductCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    product_card = models.ForeignKey('ProductCard', on_delete=models.CASCADE)
