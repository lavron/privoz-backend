import strawberry

from app.schema.types.box_type import BoxType


@strawberry.type
class BoxQuery:
    @strawberry.field
    def box(self, info) -> BoxType:
        return BoxType()
