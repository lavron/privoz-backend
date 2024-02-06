from django.contrib import admin
from django.urls import path

from app.views import game_box

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/box/', game_box, name='game_box'),
]
