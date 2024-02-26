from typing import List

import strawberry_django

from app.models import Sector
from app.strawberry_schema.types.trader_type import TraderType


@strawberry_django.type(Sector, fields="__all__")
class SectorType:
    # traders = List[TraderType]
    pass