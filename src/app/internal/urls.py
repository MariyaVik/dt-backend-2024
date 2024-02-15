from django.urls import path
from app.internal.transport.rest import handlers

urlpatterns = [
    path("me/<str:telegram_user>", handlers.me, name="me"),
]