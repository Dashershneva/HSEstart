import telebot
import flask
import random
import re

TOKEN = '311629409:AAEtJFpl4qH5BuBKjmyqoLno9y6fU4oO5aY'

"""
WEBHOOK_HOST = 'Dashershneva.pythonanywhere.com'
WEBHOOK_PORT = '443'

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

bot = telebot.TeleBot(TOKEN, threaded=False)
bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)
"""
bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я бот, и я люблю перемешивать буквы в словах")

bot.remove_webhook()

@bot.message_handler(func=lambda m: True) # здесь описываем, на какие сообщения реагирует функция
def my_function(message):
    reg = '\W'
    text = str(message.text)
    print(text)
    text_lowered = text.lower()
    text_clean = re.sub(u"\W", ' ', text_lowered)
    text_clean = text_clean.replace('  ', ' ')
    word_shuffled = []
    words = text_clean.split(' ')
    for word in words:
        symbol_list = []
        for symbol in word:
            symbol_list.append(symbol)
        text_shuffle = random.shuffle(symbol_list)
        word_shuffled.append(''.join(symbol_list))
    if text[0].isupper():
        new_text = ''.join(word_shuffled)
        i = 0
        for letter in text:
            if re.search(reg, letter):
                new_text = new_text[:i] + letter + new_text[i:]
            i += 1
        reply = new_text[0].upper() + new_text[1:]
    else:
        new_text = ''.join(word_shuffled)
        i = 0
        for letter in text:
            if re.search(reg, letter):
                new_text = new_text[:i] + letter + new_text[i:]
            i += 1
        reply = new_text
    bot.send_message(message.chat.id, reply)

bot.remove_webhook()

if __name__ == '__main__':
    bot.polling(none_stop=True)