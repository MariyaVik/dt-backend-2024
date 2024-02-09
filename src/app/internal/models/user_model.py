from django.db import models

class TelegramUser(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField()
    language_code=models.CharField(max_length=10)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        particle = '' if self.is_bot else 'не'
        return f'Пользователя {self.username} зовут {self.name}. Это {particle} бот'
    
