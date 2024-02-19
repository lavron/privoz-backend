from django.contrib import admin
from django.urls import path

# from app.views import game_box
from graphene_django.views import GraphQLView
from app.graphene_schema import schema

admin.site.site_header = "Privoz the Game"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Privoz the Game Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/box/<int:game_id>/', game_box, name='game_box'),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
