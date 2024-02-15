import re
from asgiref.sync import sync_to_async
from app.internal.models.user_model import TelegramUser


def check_phone_number(phone_number):
    pattern = r'^\+?\d{1,3}\s?\(?\d{2,3}\)?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

@sync_to_async
def get_user_count():
    count = TelegramUser.objects.count()
    print(count)
    return count

@sync_to_async
def save_phone_number(id: int, number: str):
    cur_user = TelegramUser.objects.get(id=id)
    cur_user.phone_number = number
    cur_user.save()

@sync_to_async
def check_user_phone(id: int):
    cur_user = TelegramUser.objects.get(id=id)
    if(cur_user.phone_number != None):
        return True
    else:
        return False
    
@sync_to_async
def get_user_by_id(id: int):
    return TelegramUser.objects.get(id=id)

@sync_to_async
def save_user_to_db(user: TelegramUser):
    user.save()

@sync_to_async
def check_user_existence(id: int):
    """
    Проверяет наличие записи в базе данных.
    
    Returns:
        bool: True, если запись существует, иначе False.
    """

    queryset = TelegramUser.objects.filter(id=id)
    record_exists = queryset.exists()

    return record_exists