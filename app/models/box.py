from django.db import models


class Box(models.Model):
    heroes = models.ManyToManyField('Hero', related_name='box_heroes')
    sectors = models.ManyToManyField('Sector', related_name='box_sectors')
    product_cards = models.ManyToManyField('ProductCard', related_name='box_product_cards')
    event_cards = models.ManyToManyField('EventCard', related_name='box_event_cards')

    class Meta:
        abstract = True
