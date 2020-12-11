import datetime
import ephem
from glob import glob
from random import randint, choice
from utils import get_smile,play_random_numbers, main_keyboard

def greet_user(update, context):
    print('Вызван/Start')
    username = update.effective_user.first_name
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет, {username}! {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
        )

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'{user_text} {context.user_data["emoji"]}', reply_markup=main_keyboard())

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
    update.message.reply_text(message,reply_markup=main_keyboard())

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id= chat_id, photo= open(cat_pic_filename, 'rb'), reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f'Ваши координаты {coords} {context.user_data["emoji"]}!',
        reply_markup=main_keyboard()
        )

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

def full_moon(update, context):
    print('Вызвана команда full_moon')
    user_say = update.message.text.lower()
    today = datetime.date.today()
    moon = ephem.next_full_moon(today)
    update.message.reply_text(f'Следующие полнолуние: {moon}')