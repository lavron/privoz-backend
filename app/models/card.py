from random import shuffle
from django.db import models, transaction

# LOCATION_CHOICES = [
#     ("deck", "Deck"),
#     ("hand", "Hand"),
#     ("table", "Table"),
#     ("discard", "Discard"),
# ]


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=1)
    # location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default="deck")

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
        # @todo: fix double creating of deck
        deck = cls()
        deck.save()
        deck.initialize()
        return deck

    def initialize(self):
        self.create()
        self.shuffle()

    def create(self):
        all_cards = self.card_model.objects.all()
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
    #     @todo: check if deck is created and saved at this point

    def draw_card(self):
        first_card = self.card_in_deck_model.objects.pop()
        if not self.card_in_deck_model.objects.all():
            self.initialize()

        return first_card


class CardInDeck(models.Model):
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order']
