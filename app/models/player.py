from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coins = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    premium_sector = models.ForeignKey('Sector', related_name='premium_sector', on_delete=models.CASCADE, null=True)
    event_card_protection = models.ForeignKey('EventCard', related_name='event_card_protection',
                                              on_delete=models.CASCADE, null=True)
    # traders = models.ForeignKey('Trader', related_name='player', on_delete=models.CASCADE, blank=True, default=None)

    # event_cards_new = models.ManyToManyField('EventCard', through='PlayerEventCard', related_name='players', blank=True)
    # product_cards_new = models.ManyToManyField('ProductCard', through='PlayerProductCard', related_name='players', default=None, blank=True)

    def __str__(self):
        return self.name


class PlayerEventCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    event_card = models.ForeignKey('EventCard', on_delete=models.CASCADE)


class PlayerProductCard(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    product_card = models.ForeignKey('ProductCard', on_delete=models.CASCADE)
