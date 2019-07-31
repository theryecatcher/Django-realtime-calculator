from django.urls import re_path

from .consumers import CalculatorConsumer

websocket_urlpatterns = [
    re_path(r'^ws/calculator/$', CalculatorConsumer),
]