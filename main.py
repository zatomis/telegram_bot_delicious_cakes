from telebot import TeleBot, types
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.types import ReplyKeyboardRemove
import logging
import telegram
from dotenv import load_dotenv, find_dotenv
from environs import Env

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

env = Env()
load_dotenv(find_dotenv())
bot = TeleBot(env.str('TELEGRAMBOT_KEY'))


def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Готовые торты", callback_data="ready_cake"))
    markup.add(InlineKeyboardButton("Конструктор тортов", callback_data="cake_designer"))
    markup.add(InlineKeyboardButton("О нас 😊", callback_data="info"))
    return markup

def choise_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("1", callback_data="pl1"))
    markup.add(InlineKeyboardButton("2", callback_data="pl2"))
    markup.add(InlineKeyboardButton("3", callback_data="pl3"))
    return markup


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    logger.info("Пользователь %s начал разговор", str(msg.chat.id))
    print(main_menu())
    bot.send_message(chat_id=msg.chat.id, text="Жми кнопку", reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_button_pressed(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Привет, это бот, который ....")

@bot.callback_query_handler(func=lambda call: call.data == "pl1")
def pl1_button_pressed(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Привет, это бот, который ....")
    print(call.message.text)



@bot.callback_query_handler(func=lambda call: call.data == "ready_cake")
def ready_cake_button_pressed(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("1", callback_data="ready_cake_1"))
    markup.add(InlineKeyboardButton("2", callback_data="ready_cake_2"))
    markup.add(InlineKeyboardButton("3", callback_data="ready_cake_3"))
    msg = bot.send_message(chat_id=call.message.chat.id, text="Укажи ФИО ....")
    bot.register_next_step_handler(msg, fio_step)



def fio_step(message):
    user_info = {}
    user_info['name'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите возраст')
    bot.register_next_step_handler(msg, age_step, user_info)

def age_step(message, user_info):
    user_info['age'] = message.text
    msg = bot.send_message(message.chat.id, 'Выбор ваш', reply_markup=choise_menu())
    # user_info['choise'] = message.text
    message.text = 'aaa'
    bot.register_next_step_handler(msg, choise_step, user_info)


def choise_step(message, user_info):
    user_info['choise'] = message.text

    print(user_info)
    bot.send_message(message.chat.id, str(user_info), reply_markup=main_menu())



@bot.callback_query_handler(func=lambda call: call.data == "but_1")
def button_pressed(call: types.CallbackQuery):
    print()
    # markup = InlineKeyboardMarkup()
    # markup.keyboard.remove("but_1")
    # bot.send_message(chat_id=call.message.chat.id, text="Вы нажали кнопку " + call.data + " " + str(call.message.chat.id), reply_markup: JSON.stringify({ remove_keyboard: true    }))
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    # bot.send_message(chat_id=call.message.chat.id, text="Вы нажали кнопку " + call.data + " " + str(call.message.chat.id), reply_markup=None)
    # bot.send_message(chat_id=call.message.chat.id, text="Вы нажали кнопку " + call.data + " " + str(call.message.chat.id), reply_markup=telebot.types.ReplyKeyboardRemove())
    # bot.send_message(chat_id=call.message.chat.id, text="Вы нажали кнопку " + call.data + " " + str(call.message.chat.id), reply_markup=types.ReplyKeyboardRemove()())

    user_info = {}
    user_info['name'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите возраст')
    bot.register_next_step_handler(msg, age_step, user_info)

if __name__ == '__main__':

    bot.infinity_polling(skip_pending=True)
