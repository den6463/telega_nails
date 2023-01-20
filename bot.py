import telebot
import config
import sys
from func import * 
sys.setrecursionlimit(1500)
from telebot import types #Для создания клавиатуры

bot = telebot.TeleBot(config.TOKEN)

def chat_bot(message):
   if message.chat.type == 'private':
      if message.text == "Адрес":
         adres(message)
   if message.chat.type == 'private':
      if message.text == "/start":
         main_menu(message)
   if message.chat.type == 'private':
      if message.text == "Порядок приема":
         poryadok_priema(message)
   if message.chat.type == 'private':
      if message.text == "Факультеты":
         fakultet(message)
   if message.chat.type == 'private':
      if message.text == "Университет":
         universitet(message)
   if message.chat.type == 'private':
      if message.text == "Довузовская подготовка":
         dovuz_podgotovka(message)
   if message.chat.type == 'private':
      if message.text == "Военная кафедра":
         voen_kafedra(message)
   if message.chat.type == 'private':
      if message.text == "Проф. Тест":
         que_one_res()
         que_two_res()
         prof(message)
         otvet()
         otvet_tg(message)

   else: bot.send_message(message.chat.id, "К сожалению, я Вас не понимаю")

bot.polling(none_stop=True)