import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import (greet_user, talk_to_me, guess_number, send_cat_picture,
                        user_coordinates, planet_pos, full_moon)
import settings


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_pos))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(CommandHandler('next_full_moon',full_moon))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'),send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == '__main__':
    main()