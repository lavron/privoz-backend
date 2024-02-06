from django.db import models
# from .player import Player


class Game(models.Model):
    players = models.ManyToManyField('Player', related_name='games')
    sectors = models.ManyToManyField('Sector', related_name='games')
    product_cards = models.ManyToManyField('ProductCard', related_name='games')
    event_cards = models.ManyToManyField('EventCard', related_name='games')

    def __str__(self):
        return self.pk + '. ' + self.players


