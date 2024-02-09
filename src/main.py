
import os
import django

from src.app.internal.transport.bot.handlers import *

# СДЕЛАТЬ РУЧКУ

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
from config.settings import env

def main():
    print('start')

    print(env('MY_BOT_TOKEN'))

    application = ApplicationBuilder().token('6661752125:AAEveZPm9GPvlAbHvcNaBQg-pGL5dmiQxy4').build()
    # application = ApplicationBuilder().token(env('MY_BOT_TOKEN')).build()
    
    start_handler = CommandHandler('start', start)
    phone_handler = CommandHandler('set_phone', set_phone)
    me_handler = CommandHandler('me', me)
    echo_handler = MessageHandler(filters.TEXT | filters.COMMAND, echo)
    caps_handler = CommandHandler('caps', caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    
    application.add_handler(start_handler)
    application.add_handler(phone_handler)
    application.add_handler(me_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()

if __name__ == '__main__':
   main()