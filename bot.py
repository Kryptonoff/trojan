import telebot
import pyautogui
import win32api, win32con, win32gui
import os
from telebot import types
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# настройка
bot = telebot.TeleBot('ТОКЕН')
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# функции
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Скриншот")
    btn2 = types.KeyboardButton("Выключить звук")
    btn3 = types.KeyboardButton("Выключить экран")
    btn4 = types.KeyboardButton("Выключить компьютер")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Хулиганим", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Скриншот':
        pyautogui.screenshot('screenshot.png',region=(0,0, 1920, 1080))
        bot.send_photo(message.from_user.id, photo=open('screenshot.png', 'rb'))
    
    if message.text == 'Выключить звук':
        volume.SetMasterVolumeLevel(-60.0, None) #max

    if message.text == 'Выключить экран':
        win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

    if message.text == 'Выключить компьютер':
        os.system('shutdown -s')

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)