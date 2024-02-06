from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=100)

    class Meta:
        abstract = True
