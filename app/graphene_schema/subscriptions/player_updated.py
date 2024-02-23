import graphene

from app.models import Player
from app.graphene_schema.types.player_type import PlayerType


#
# class PlayerUpdatedSubscription(graphene.ObjectType):
#     player_updated = graphene.Field(PlayerType)
#
#     def resolve_player_updated(root, info, id):
#         return root.filter(
#             lambda event: event.operation == UPDATED
#                           and isinstance(event.instance, Player)
#                           and event.instance.pk == int(id)
#         ).map(lambda event: event.instance)