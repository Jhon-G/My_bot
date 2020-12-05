from emoji import emojize
from glob import glob
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime
from random import randint, choice

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван/Start')
    username = update.effective_user.first_name
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет, {username}! {context.user_data["emoji"]}')

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'{user_text} {context.user_data["emoji"]}')

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def planet_pos(update, context):
    print('Взвана/Planet')
    user_say = update.message.text.lower()
    if user_say == '/planet':
        planet_list = ephem._libastro.builtin_planets()[:10] #Список из 10 планет
        stars_list = []
        for i in planet_list:
            for name in i[2:3]:
                stars = name
            stars_list.append(stars) # Выводим список планет 1 сообщением
        update.message.reply_text(f'Напиши название планеты или звезды. /planet {stars_list}')
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

def guess_number(update, context):
    print(context.args)
    if context.args:
        try :
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число ' 
    else:
        message = 'Введите число'
    update.message.reply_text(message)

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!'
    elif user_number == bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ничья!'
    else:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, я выиграл!'
    return message


def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id= chat_id, photo= open(cat_pic_filename, 'rb'))

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_pos))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == '__main__':
    main()