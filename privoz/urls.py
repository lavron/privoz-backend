from django.contrib import admin
from django.urls import path

from app.views import game_box

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/box/<int:game_id>/', game_box, name='game_box'),
]
