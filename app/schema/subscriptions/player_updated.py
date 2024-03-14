import graphene

from app.models import Player
from app.schema.types.player_type import PlayerType
from rx import Observable
from graphene_subscriptions.events import CREATED, UPDATED, DELETED


class PlayerUpdatedSubscription(graphene.ObjectType):
    player_updated = graphene.Field(PlayerType)

    def resolve_player_updated(root, info, id):
        return root.filter(
            lambda event: event.operation == UPDATED
                          and isinstance(event.instance, Player)
                          and event.instance.pk == int(id)
        ).map(lambda event: event.instance)


import graphene import django_channels_graphql_ws

class OnPlayerUpdated(django_channels_graphql_ws.Subscription):
    """Subscription triggers on a player update."""
    player = graphene.Field(PlayerType)
    class Arguments:
        player_id = graphene.ID()

    def subscribe(self, info, player_id):
        """Client subscription request handling."""
        # Specify the subscription group
        return [f"player_{player_id}"]

    def publish(self, info, player_id):
        """Called to prepare the broadcast message."""
        # Fetch the updated instance of the player.
        try:
            player = Player.objects.get(pk=player_id)
        except Player.DoesNotExist:
            return OnPlayerUpdated(player=None)

        return OnPlayerUpdated(player=player)