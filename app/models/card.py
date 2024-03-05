from django.db import models


class BaseCard(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=100, blank=True)
    quantity_in_deck = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    # @classmethod
    # def get_in_desk_model(cls):
    #     raise NotImplementedError("This method should be implemented in subclasses.")

#
# class CardInGame(models.Model):
#     is_discarded = models.BooleanField(default=False)
#     order = models.IntegerField(default=0)
#     # card = models.ForeignKey(BaseCard, on_delete=models.CASCADE)
#     # game = models.ForeignKey('Game', on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['order']

