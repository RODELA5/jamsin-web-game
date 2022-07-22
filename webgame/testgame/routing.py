from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/testgame/', consumers.TestgameConsumer.as_asgi()),
]
