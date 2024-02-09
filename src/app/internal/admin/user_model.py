from django.contrib import admin

from app.internal.models.user_model import TelegramUser


@admin.register(TelegramUser)
class AdminTelegramUser(admin.ModelAdmin):
    pass