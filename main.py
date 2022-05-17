import telebot
from config import keys, TOKEN
from Class import CryptoConverter, ConvertionException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f'Добро пожаловать, {message.from_user.full_name}\nПеред началом работы нажми на: /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = f'Что бы начать работу введити команду в следующем формате:\n<название валюты> \
<в какую валюту переводим> \
<количество валюты>\nЧто бы увидеть список доступных валют нажмите на: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Не верное количество параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду:\n{e}')
    else:
        total_price = round((float(amount) * float(total_base)),2)
        text = f'Цена {amount} {quote} в {base} - {total_price}'
        bot.send_message(message.chat.id, text)


bot.polling()
