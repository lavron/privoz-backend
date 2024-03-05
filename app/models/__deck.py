from django.db import models, transaction
from random import shuffle


class BaseDeck(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    @transaction.atomic
    def create_new_deck(card_model):
        deck = BaseDeck()
        deck.create_cards(card_model)
        deck.shuffle()
        deck.save()
        return deck

    @classmethod
    def create_cards(cls, card_model):
        card_bases = card_model.objects.all()
        card_in_desk_model = card_model.get_in_desk_model()

        cards = []
        for card in card_bases:
            for _ in range(card.quantity_in_deck):
                cards.append(card_in_desk_model(card=card, deck=cls))
        card_in_desk_model.objects.bulk_create(cards)


    @classmethod
    def shuffle(cls):
        card_model = cls.get_card_model()
        card_in_desk_model = card_model.get_in_desk_model()
        deck = card_in_desk_model.objects.filter(deck_id=cls.id)
        shuffle(deck)
        cards = card_in_desk_model.objects.all()
        shuffle(cards)
        for card in cards:
            card.is_discarded = False
        card_in_desk_model.objects.bulk_update(cards, ['is_discarded'])

    @classmethod
    def draw_cards(cls, count):
        cards = []
        for _ in range(count):

            top_card = cls.cards.order_by('id').first()
            cards.append(top_card)
            top_card.is_discarded = True
            top_card.save()

            cards_left = cls.get_in_desk_model().objects.all()
            if not cards_left:
                cls.shuffle()

        return cards

    def __str__(self):
        name = 'Deck ' + str(self.id)
        if hasattr(self, 'cards'):
            name += ' (' + str(self.cards.count()) + ' cards)'
        return name

    @classmethod
    def get_card_model(cls):
        raise NotImplementedError("This method should be implemented in subclasses.")


