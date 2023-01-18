import telebot
bot = telebot.TeleBot('5747207857:AAH0F8fGDmXFfmGAkA7A-lKXhVhoS_elAc8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
      
bot.polling(none_stop=True, interval=0)