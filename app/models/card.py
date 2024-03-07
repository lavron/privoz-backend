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