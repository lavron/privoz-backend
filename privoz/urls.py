from django.contrib import admin
from django.urls import path
from strawberry.django.views import AsyncGraphQLView

from app.root_schema import schema
from privoz import settings

admin.site.site_header = "Privoz the Game"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Privoz the Game Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'graphql/',
        AsyncGraphQLView.as_view(
            schema=schema,
            graphiql=settings.DEBUG,
            subscriptions_enabled=True,
        ),
    ),]
