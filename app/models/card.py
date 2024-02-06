from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        caller = self._meta.model_name
        return self.name + ' - ' + caller

    class Meta:
        abstract = True
