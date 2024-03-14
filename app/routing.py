# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
#
# from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer
#
# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         path('graphql/', GraphqlSubscriptionConsumer)
#     ]),
# })

from django.conf.urls import url
from graphene_django.views import GraphQLView
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url('graphql', GraphQLView.as_view(graphiql=True)),
        ])),
})
