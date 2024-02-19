from app.schema.types.box_type import BoxType
from app.models import Hero, Sector, ProductCard, EventCard


class BoxService:
    @staticmethod
    def get_content():
        return BoxType(
            heroes=Hero.objects.all(),
            sectors=Sector.objects.all(),
            product_cards=ProductCard.objects.all(),
            event_cards=EventCard.objects.all()
        )
