import json
from django.http import HttpResponse, JsonResponse

from app.internal.models.user_model import TelegramUser
from app.internal.services.user_serializer import UserSerializer


def me(request, telegram_user):
    queryset = TelegramUser.objects.filter(username=telegram_user)
    record_exists = queryset.exists()
    if record_exists:
        user = TelegramUser.objects.get(username=telegram_user)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(f"Пользователя {telegram_user} нет в нашей базе")