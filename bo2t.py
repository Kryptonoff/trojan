import telebot

# настройка
bot = telebot.TeleBot('5747207857:AAH0F8fGDmXFfmGAkA7A-lKXhVhoS_elAc8')

# функции
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Скриншот")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Хулиганим", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Скриншот':
	ot.send_message(message.from_user.id, "Хулиганим", reply_markup=markup)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
