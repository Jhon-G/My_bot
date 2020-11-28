import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_pos))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


def greet_user(update, context):
    print('Вызван/Start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def planet_pos(update, context):
    print('Взвана/Planet')
    user_say = update.message.text.lower()
    if user_say == '/planet':
        planet_list = ephem._libastro.builtin_planets()[:10] #Список из 10 планет
        for i in planet_list:
            for name in i[2:3]:
                stars = name
                update.message.reply_text(f'Напиши название планеты или звезды. /planet {stars}')
    user_say = update.message.text.split()
    today = datetime.date.today()
    if user_say[1].capitalize() == 'Mercury':
        const = ephem.constellation(ephem.Mercury(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Venus':
        const = ephem.constellation(ephem.Venus(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Mars':
        const = ephem.constellation(ephem.Mars(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Jupiter':
        const = ephem.constellation(ephem.Jupiter(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Saturn':
        const = ephem.constellation(ephem.Saturn(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Uranus':
        const = ephem.constellation(ephem.Uranus(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Neptune':
        const = ephem.constellation(ephem.Neptune(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Pluto':
        const = ephem.constellation(ephem.Pluto(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Sun':
        const = ephem.constellation(ephem.Sun(today))
        update.message.reply_text(const)
    elif user_say[1].capitalize() == 'Moon':
        const = ephem.constellation(ephem.Moon(today))
        update.message.reply_text(const)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


if __name__ == '__main__':
    main()