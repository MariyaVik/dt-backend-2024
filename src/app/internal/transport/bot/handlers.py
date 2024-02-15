from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes
from app.internal.models.user_model import TelegramUser
from app.internal.services.user_service import *
from app.internal.services.logger import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_db = TelegramUser(name=user.first_name, is_bot=user.is_bot, language_code=user.language_code, username=user.username, id=user.id)
    if (not await check_user_existence(user.id)):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba!\n\nЗдравствуйте!")
        await save_user_to_db(user_db)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sizi veritabanına ekledim\n\nЯ добавил Вас в базу данных")
        btns = [KeyboardButton(text="/set_phone")]
        keyboard = [btns]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True)

        await update.message.reply_text('Devam etmek için telefon numaranızı girmelisiniz (/set_phone)\n\nДля продолжения необходимо ввести свой номер телефона (/set_phone)', reply_markup=reply_markup)
        # await context.bot.send_message(chat_id=update.effective_chat.id, text="Devam etmek için telefon numaranızı girmelisiniz")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Zaten konuştuk\n\nМы уже общались")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(user)
    if (await check_user_phone(user.id)):
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Anlamıyorum. Sorunu @MariyaViktorovna yazın\n\nЯ не понимаю Вас. Напишите свой вопрос @MariyaViktorovna')
    else:
        if check_phone_number(update.message.text):
            await save_phone_number(user.id,  update.message.text)
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Telefon numaranız veritabanına kaydedilir\n\nВаш номер телефона сохранён в базе данных')
            btns = [KeyboardButton(text="/me")]
            keyboard = [btns]
            reply_markup = ReplyKeyboardMarkup(keyboard=keyboard)

            await update.message.reply_text('Kendinizle ilgili bilgileri görüntüleyebilirsiniz (/me)\n\nВы можете просмотреть информацию о себе (/me)', reply_markup=reply_markup)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Geçersiz telefon numarası\n\nНекорректный номер телефона')

async def set_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if (await check_user_phone(user.id)) :
        await update.message.reply_text(text='Veri tabanında telefon numaranız var\n\nВаш номер телефона есть в базе')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Telefon numaranızı girin\n\nВведите свой номер телефона')
        echo(Update, ContextTypes.DEFAULT_TYPE)

async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if (await check_user_existence(user.id)):
        if (await check_user_phone(user.id)) :
            cur_user = await get_user_by_id(user.id)
            particle_t = 'botsunuz' if cur_user.is_bot else 'bot değilsiniz'
            particle_r = '' if cur_user.is_bot else 'не'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''
    Verileriniz:
        * Adınız - {cur_user.name}
        * Telefon numaranız - {cur_user.phone_number}
        * Takma adınız - @{cur_user.username}
        * Ve siz {particle_t}

    Ваши данные:
        * Имя - {cur_user.name}
        * Номер телефона - {cur_user.phone_number}
        * Никнейм - @{cur_user.username}
        * И Вы {particle_r} бот
    ''')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Devam etmek için telefon numaranızı girmelisiniz\n\nДля продолжения необходимо ввести свой номер телефона')
            echo(Update, ContextTypes.DEFAULT_TYPE)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Veritabanımızda değilsiniz. Hadi tanışalım!\n/start komutunu girin\n\nВас нет в нашей базе. Давайте знакомиться!\nВведите команду /start ')

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ben anlamıyorum :(\n\nЯ не понимаю :(")
