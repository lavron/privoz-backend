import graphene

from app._del_graphene_schema.types.box_type import BoxType
from app._del_graphene_schema.services.box_service import BoxService

box_service = BoxService()

class BoxQuery(graphene.ObjectType):
    content = graphene.Field(BoxType)

    @staticmethod
    def resolve_content(root, info):
        return box_service.get_content()

