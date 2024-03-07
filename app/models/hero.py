from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=20)
    image = models.CharField(max_length=200, blank=True)
    premium_sector = models.ForeignKey('BaseSector', related_name='hero', on_delete=models.CASCADE, null=True)
    event_card_protection = models.ForeignKey('Event', related_name='hero',
                                              on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
