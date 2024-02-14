from random import shuffle

from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=1, db_default=1)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Deck(models.Model):
    card_model = Card
    cards = []

    class Meta:
        abstract = True

    def __str__(self):
        return 'Deck ' + str(self.pk)

    def __init__(self, *args, **kwargs):
        self.card_model = kwargs.pop('card_model', Card)
        print("👉🏻self.card_model", self.card_model)
        super().__init__()
        self.create()
        self.shuffle()

    def create(self, *args, **kwargs):
        all_cards = self.card_model.objects.all()
        deck_cards = []
        for card in all_cards:
            for _ in range(card.quantity):
                deck_cards.append(card)
        self.cards = deck_cards

    def shuffle(self):
        shuffle(self.cards)
