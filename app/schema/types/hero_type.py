import strawberry_django

from app.models import Hero

@strawberry_django.type(Hero, fields="__all__")
class HeroType:
    pass
