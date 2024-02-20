# views.py
from graphene_django.views import GraphQLView

from app.events import player_updated
from app.graphene_schema import schema


def graphql_view(request):
    player_updated.on_next('Player updated')
    view = GraphQLView.as_view(schema=schema)
    return view(request)
