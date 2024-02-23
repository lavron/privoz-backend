import strawberry_django

from app.models import Sector

@strawberry_django.type(Sector, fields="__all__")
class SectorType:
    pass