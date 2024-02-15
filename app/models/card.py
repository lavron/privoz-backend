from random import shuffle
from django.db import models, transaction


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
    class Meta:
        abstract = True

    def __str__(self):
        return 'Deck ' + str(self.id)

    def __init__(self, *args, **kwargs):
        self.card_model = kwargs.pop('card_model', None)
        self.card_in_deck_model = kwargs.pop('card_in_deck_model', None)
        super().__init__(*args, **kwargs)


    @classmethod
    @transaction.atomic
    def create_and_initialize(cls):
        deck = cls()
        deck.save()
        deck.initialize()
        return deck

    def initialize(self):
        if self.card_model and self.card_in_deck_model:
            self.create()
            self.shuffle()
            self.save()
        else:
            raise ValueError("card_model and card_in_deck_model must be set")

    def create(self):
        all_cards = self.card_model.objects.all()
        print("👉🏻create all_cards", all_cards)
        card_in_deck_instances = []
        for index, card in enumerate(all_cards):
            for _ in range(card.quantity):
                card_in_deck_instances.append(self.card_in_deck_model(card=card, deck=self, order=index))
        if card_in_deck_instances:
            self.card_in_deck_model.objects.bulk_create(card_in_deck_instances)

    def shuffle(self):
        card_in_deck_instances = list(self.card_in_deck_model.objects.all())
        shuffle(card_in_deck_instances)
        for order, instance in enumerate(card_in_deck_instances):
            instance.order = order
            instance.save()
        print("👉🏻shuffle card_in_deck_instances", card_in_deck_instances)


class CardInDeck(models.Model):
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order']
