import telebot
import random
import os

a = ["переводчиком","КНБ-шником","министром","дипломатом","юристом", "журналистом", "археологом","архитектором","дизайнером",
     "спасателем","психологом","адвокатом", "судьёй","спортсменом", "режиссером", "прокурором","врачом","доктором", "полицейским","инженером", "программистом",
     "экономиком", "таксистом", "учительем", "пилотом","поваром", "тренером", "продавцом", "уборщиком", "актером", "фермером" ,  "бизнесменом","менеджером","профессором"]
b = ["Айдын", "Мирас", "Нурсат","Жанибек","Рахман","Олжас","Дарын","Бектас","Ислам","Санжар","Ерасыл","Асылхан","Нуржан","Бакдаулет","Алимжан","Арсен","Бекнур","Бексултан","Магжан",
     "Елнур","Рустем","Рамазан","Молшылык","Димаш","Нурсултан","Аскар","Алишер","Арман","Алмас"]
c = ["Айгерим", "Аружан", "Томирис","Анелья", "Софа", "Салтанат","Настя", "Дина", "Диана","Жанна","Амина","Алуа","Айсулу","Мадина","Айзере","Жанель",
     "Камила","Ляззат", "Дарига","Анджелина"]
bot_token = os.environ['BOT_TOKEN']

from telebot import types


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Привет,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы служить.\n(created by @idon2003)  ". format(message.from_user,bot.get_me()), parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Имя второй половинки")
    item2 = types.KeyboardButton("Когда поженишься")
    item3 = types.KeyboardButton("Сколько детей будет")
    item4 = types.KeyboardButton("Будущую профессию")

    markup.add(item1,item2,item3, item4)

    bot.send_message(message.chat.id,"Выбери пункт который тебя интересует \n Ты можешь узнать ".format(message.from_user,bot.get_me()),
                     parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message, ):
    if message.chat.type == 'private':
        if message.text=='Имя второй половинки':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Парень", callback_data='man')
            item2 = types.InlineKeyboardButton("Девушка", callback_data='woman')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Выберите свой пол",reply_markup=markup)


            bot.send_message(message.chat.id,"Имя твоей второй половинки :")

        elif message.text=='Когда поженишься':
            bot.send_message(message.chat.id,"Ты поженишься в" ' ' + str(random.randint(19,32)) )
        elif message.text=='Сколько детей будет':
            bot.send_message(message.chat.id," У тебя будет" ' '+ str(random.randint(2,5))+ ' ' "ребенка")
        elif message.text == 'Будущую профессию':
            bot.send_message(message.chat.id,"Ты станешь отличным" ' ' +  random.choice(a))
        else:
            bot.send_message(message.chat.id,'Я не знаю ответ на твой вопрос' + "\N{pensive face}")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'man':
                bot.send_message(call.message.chat.id,random.choice(c))
            elif call.data == 'woman':
                bot.send_message(call.message.chat.id,random.choice(b))


            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Выберите пол",
                                  reply_markup=None)


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True, interval=0)
