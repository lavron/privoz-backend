import strawberry

from app.strawberry_schema.types.box_type import BoxType


@strawberry.type
class BoxQuery:
    @strawberry.field
    async def box(self, info) -> BoxType:
        box = BoxType()
        await box.heroes(info)
        await box.sectors(info)
        await box.product_cards(info)
        await box.event_cards(info)
        return box