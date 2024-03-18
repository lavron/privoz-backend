from django.urls import re_path
from graphene_django.views import GraphQLView
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    # 'http': get_asgi_application(),
    'websocket': URLRouter([
        re_path('graphql', GraphQLView.as_view(graphiql=True)),
    ]),
})