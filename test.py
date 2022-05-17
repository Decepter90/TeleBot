import telebot
from telebot import types
from config import keys, TOKEN



def start(message: telebot.types.Message):
    text = f'Добро пожаловать, {message.from_user.full_name}\nНажмите одну из кнопок:'
    bot.reply_to(message, text, reply_markup = markup)


def help(bot, update):
    update.message.reply_text('')

def phone(bot, update):
    update.message.reply_text('Телефон: +86 133 2686 8519')


reply_keyboard = [['/help', '/values']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('close', close_keyboard))

dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('values', values))

dp.add_handler(text_handler)

