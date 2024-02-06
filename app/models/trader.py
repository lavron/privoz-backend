from django.db import models


class Trader(models.Model):
    player = models.OneToOneField('Player', related_name='trader', on_delete=models.CASCADE)
    sector = models.ForeignKey('Sector', related_name='traders', on_delete=models.CASCADE)
    products = models.ManyToManyField('ProductCard', related_name='traders')
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
