import telebot
import config
import sqlite3
from telebot import types #Для создания клавиатуры

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def main_menu(message):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Авторазмер клавиатуры
   item1 = types.KeyboardButton("Информация о салоне")
   item2 = types.KeyboardButton("Маникюр")
   item3 = types.KeyboardButton("Тест тип маникюра")
   item4 = types.KeyboardButton("Педикюр")
   item5 = types.KeyboardButton("Массаж")
   item6 = types.KeyboardButton("Режим работы")
   item7 = types.KeyboardButton("Ситрижки")
   markup.add(item1, item2, item3, item4, item5, item6, item7)
   bot.send_message(message.chat.id, "Поздравляю, {0.first_name}!\nЯ - {1.first_name}, а Вы в главном меню!.".format(message.from_user, bot.get_me()), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def fakultet(message):         ##Стрижка
   if message.chat.type == 'private':
      if message.text == 'Ситрижки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Блант боб")
            item2 = types.KeyboardButton("Каре")
            item3 = types.KeyboardButton("Маллет")
            item4 = types.KeyboardButton("Химэ")
            item5 = types.KeyboardButton("Каскад")
            item6 = types.KeyboardButton("В главное меню")

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, "Вам представлены самые популярные стрижки, пожалуйста, уточните, какой именно Вас интересует?", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Блант боб':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            f = open ("files//pic//blant.jpg", "rb")
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id,"Одна из самых популярных стрижек на сегодняшний день — это короткое каре или боб с прямым или даже слегка небрежным срезом.", f, reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Каре':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            f = open ("files//pic//kare.jpg", "rb")
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id,"Каре — в целом очень модная стрижка в последние годы. Просто разные вариации этой прически становятся то более, то менее актуальными в каждый конкретный сезон. Например, сейчас рекомендуется обратить внимание на каре в стиле 90-х.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Маллет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            f = open ("files//pic//mallet.jpg", "rb")
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id,"Популярная в 70-е и 80-е годы стрижка маллет снова стала модной в 2023 году. Маллет — это стрижка с челкой и волосами, прикрывающими шею.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Химэ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            f = open ("files//pic//xime.jpg", "rb")
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id,"Стрижка химэ выполняется на средние или длинные волосы. Она предполагает челку и срез части волос у подбородка.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Каскад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            f = open ("files//pic//kaskad.jpg", "rb")
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id,"Универсальная стрижка каскад идеально подходит как на длинные и средние волосы, так и на короткие. Такая стрижка способна скорректировать черты лица, скрыть недостатки и подчеркнуть достоинства.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : poryadok_priema(message)

@bot.message_handler(content_types=['text'])
def poryadok_priema(message):           ##Информация о салоне
   if message.chat.type == 'private':
      if message.text == "Информация о салоне":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Контакты")
            item2 = types.KeyboardButton("Наши мастера")
            item3 = types.KeyboardButton("Цены")
            item4 = types.KeyboardButton("В главное меню")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "ИНформация о салоне", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Контакты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Мы находимся по адрусу Ул. Пушкина дом Колотушкина 27. Контакный номер +71111111111", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Наши мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Кузмичева Е.А. Парикмахер-универсал Опыт работы 25 лет. \n\n Пушкина Д.Д. Мастер маникюра  Опыт работы 5 лет. \n\nИгорев А.В. Массажист   \n\n Опыт работы 10 лет", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Цены':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Наши цены на настоящее время:", reply_markup=markup)
            f = open("files//pic//zena.jpg","rb")
            bot.send_photo(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : adres(message)

@bot.message_handler(content_types=['text'])
def adres(message):                      ##Маникюр
   if message.chat.type == 'private':
      if message.text == "Маникюр":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Классический маникюр")
         item2 = types.KeyboardButton("Японский манкюр")
         item3 = types.KeyboardButton("Бразильский манкюр")
         item4 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4)
         bot.send_message(message.chat.id, "Выбирете униврситет", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Классический маникюр':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"Классический маникюр начинают с корректировки формы ногтей. Далее, перед обработкой кутикулы, выполняют мацерацию — делают ванночку для размягчения кожи.", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Бразильский манкюр':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"В этом виде маникюра и педикюра акцент тоже сделан на уход. А еще — на безопасность: в нем не используются ножницы, щипчики, шабер с острым «топориком» на конце — повредить кожу или ногти в бразильском маникюре просто не получится.", reply_markup=markup)

   if message.chat.type == 'private':
      if message.text == 'Японский манкюр':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id,"Эта техника — особый ритуал, который идеально подойдет тем, кто любит максимально естественный маникюр, а также легко обходится без покрытия.", reply_markup=markup)
   if message.chat.type == 'private':
      if message.text == 'В главное меню' :
         main_menu(message)
      else : voen_kafedra(message)

@bot.message_handler(content_types=['text'])
def voen_kafedra(message):                  ##педикюр
   if message.chat.type == 'private':
      if message.text == "Военная кафедра":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Классический педикюр")
         item2 = types.KeyboardButton("Экспресс-педикюр")
         item3 = types.KeyboardButton("Кислотный педикюр")
         item4 = types.KeyboardButton("Спа-педикюр")
         item5 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4, item5)
         bot.send_message(message.chat.id, "Постановлением Совета Министров Республики Беларусь от 14 апреля 2020 года № 220 «Об изменении в постановление Совета Министров Республики Беларусь от 5 ноября 2003 года № 1469» учреждение образования «Брестский государственный технический университет» включен в Перечень учреждений высшего и среднего специального образования, в которых проводится обучение граждан на военных кафедрах.", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Классический педикюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Это самый популярный вид педикюра, назовем его old-fashioned. Классический педикюр еще называют обрезным. Сделайте ванночку с теплой водой и разведите в ней соль, чтобы размягчить кутикулы и кожу пяток. Кутикулу мастер удаляет с помощью кусачек, а лишнюю кожу с пяток, мелкие натоптыши и мозоли – специальной пилкой для шлифовки.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Экспресс-педикюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Если вы видите в меню пункт «экспресс-педикюр», скорее всего, это означает только работу с ногтями, то есть снятие покрытия, быструю обработку ногтей и покрытие лаком. Никаких ванночек с солью – такой педикюр подойдет или вечно занятым бизнес-леди, или тем, кто меняет цвет лака каждую неделю.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Кислотный педикюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Еще такой вид педикюра называют Kart или ADN – по названию марок, которые производят специальные растворы для педикюра с кислотами. Суть техники состоит в том, что раствор «разъедает» ороговевшие частички кожи и порой даже не включает обработку кожи пилкой. То, что нужно для обладателей тонкой и чувствительной кожи.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'Спа-педикюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id,"Пилинги, скрабы, маски, носочки, массаж и непременно ароматерапия – после спа-педикюра вы выходите не только с новым педикюром, но и с ощущением, будто вы побывали на побережье Индийского или Атлантического океана. Смотря какие средства использовал мастер во время процедуры. Под спа-педикюром понимается и бразильский педикюр (вместо ванночки мастер надевает на вас носочки со специальным лосьоном, который смягчает натоптыши и кутикулу), и так называемый детокс-педикюр – с частичками черного угля, а также бананово-кокосовый. По времени такая процедура педикюра длится чуть дольше обычного.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : dovuz_podgotovka(message)

@bot.message_handler(content_types=['text'])
def dovuz_podgotovka(message):                ##Массаж
   if message.chat.type == 'private':
      if message.text == "Массаж":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("БАЛИЙСКИЙ МАССАЖ")
         item2 = types.KeyboardButton("АРОМАТИЧЕСКИЙ МАССАЖ")
         item3 = types.KeyboardButton("РЕФЛЕКТОРНО-СЕГМЕНТАРНЫЙ МАССАЖ")
         item4 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4)
         bot.send_message(message.chat.id,"Довуз.подготовка", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'БАЛИЙСКИЙ МАССАЖ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "Его особенность - в глубоком точечном воздействии на мышцы. Именно этот вид массажа представляет собой микс шведского массажа, акупрессуры, ароматерапии и индийской аювердической медицины.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'АРОМАТИЧЕСКИЙ МАССАЖ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "Сеанс Рани — это исключительно индивидуальный подход. Изучая физического состояние каждого пациента, его настроение и энергетическое поле, он по показаниям подбирает технику массажа, а также смесь эфирных масел. Воздействие ведется не только на физическом, но также психо-эмоциональном уровне — сеанс призван избавить не только от мышечной усталости, но также решить целый ряд самых сложных проблем, связанных с похудением, увеличением потенции, улучшением настроения, борьбой с бессоницей, снижением аппетита и многих других.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'РЕФЛЕКТОРНО-СЕГМЕНТАРНЫЙ МАССАЖ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "Рефлекторно-сегментарный массаж - это классическая лечебная техника, придуманная врачами. Принцип его заключается в воздействии на определенные участки тела, которые с помощью нервных окончаний связаны с внутренними органами и позвоночником.", reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : universitet(message)

@bot.message_handler(content_types=['text'])
def universitet(message):                     ##Режим работы     
   if message.chat.type == 'private':
      if message.text == "Режим работы":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Парикмахерская")
         item2 = types.KeyboardButton("Маникюр")
         item3 = types.KeyboardButton("Педикюр")
         item4 = types.KeyboardButton("Массаж")
         item5 = types.KeyboardButton("В главное меню")
         markup.add(item1, item2, item3, item4, item5)
         bot.send_message(message.chat.id,"Основная информация по салону красоты", reply_markup=markup)

      if message.chat.type == 'private':
         if message.text == 'Парикмахерская':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "График работы парикмахеров", reply_markup=markup)
            f= open("files//pic//graf_parik.jpg","rb")
            bot.send_photo(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Маникюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "График работы мастеров маникюра", reply_markup=markup)
            f= open("files//pic//graf_parik.jpg","rb")
            bot.send_photo(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Педикюр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "График работы мастеров педикюра", reply_markup=markup)
            f= open("files//pic//graf_parik.jpg","rb")
            bot.send_photo(message.chat.id,f)
      if message.chat.type == 'private':
         if message.text == 'Массаж':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("В главное меню")
            markup.add(item1)
            bot.send_message(message.chat.id, "График работы массажиста: \n Пн-Пт 10:00-20:00", reply_markup=markup)            
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
         else : prof(message)

conect = sqlite3.connect("test.db", check_same_thread=False)
cursor = conect.cursor()
conect.commit()
a= 0
n= ""
m= ""
marks = '''()'",'''
def que_one_res():
   global m
   cursor.execute("SELECT que_one FROM test")
   res_one = cursor.fetchall()
   m = res_one[a]
   m= str(m)
   for x in m:  
      if x in marks:  
         m = m.replace(x, "") 
def que_two_res():
   global n
   cursor.execute("SELECT que_two FROM test")
   res_two = cursor.fetchall()
   n = res_two[a]
   n = str(n)
   for x in n:  
      if x in marks:  
         n = n.replace(x, "") 
que_one_res()
que_two_res()
first_count= 1
second_count= 1
que_count = 0

@bot.message_handler(content_types=['text'])
def prof(message):
   global a, first_count, second_count, que_count
   if message.chat.type == 'private':
      if message.text == 'Тест тип маникюра':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print(n,m)
   if message.chat.type == 'private':
      if message.text == n:
         second_count += 1
         que_count +=1
         a+=1
         que_one_res()
         que_two_res()
         print (n,m)
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print ("Очки 2 вопроса:",second_count)
         print ("Всего вопросов:",que_count)
         if que_count == 14:
            otvet_tg(message)

   if message.chat.type == 'private':
      if message.text == m:
         first_count += 1
         que_count +=1
         a+=1
         que_one_res()
         que_two_res()
         print (n,m)
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton(text= m)
         item2 = types.KeyboardButton(text= n)
         markup.add(item1, item2)
         bot.send_message(message.chat.id, "Выбери то, что тебе ближе", reply_markup=markup)
         print ("Очки 1 вопроса:",first_count)
         print ("Всего вопросов:",que_count)
         if que_count == 14:
            otvet_tg(message)
def otvet():
   global tip
   percent = (first_count/que_count)*100
   if percent < 20:
      tip = ("нежный маникюр")
   if 20< percent < 40:
      tip = ("яркий и броский маникюр")
   if 40< percent < 70:
      tip = ("маникюр в нюдовых тонах")
   if 70< percent < 100:
      tip = ("необычный, узорчатый маникюр")
   if 100< percent:
      tip = ("спокойный, сдержанный маникюр")
tip = ""
tip = str(tip)
@bot.message_handler(content_types=['text'])
def otvet_tg(message): 
   global a, first_count, second_count, que_count, tip
   otvet()
   if message.chat.type == 'private':
      if message.text == "Нюдовые тона" or "Френч или несложный дизайн":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("В главное меню")
         markup.add(item1)
         bot.send_message(message.chat.id, "Поздравляю, Вам подойдет " + tip, reply_markup=markup)
      if message.chat.type == 'private':
         if message.text == 'В главное меню' :
            main_menu(message)
bot.polling(none_stop=True)