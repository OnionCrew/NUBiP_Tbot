import telebot
from telebot import types
import time


bot = telebot.TeleBot('6135314118:AAHkksZtMolECCUQXFGexkJNYqbhrDpYyWA')

@bot.message_handler(commands=["start"])
def start(message, res=False):
        markup=types.ReplyKeyboardMarkup(True,False)
        markup.row('Підтримка🛠','Розклад 🗓','Бомбосховища⚠️')
        markup.add('Новини університету📰')
        bot.send_message(message.chat.id, 'Ласкаво просимо ❗️\nВиберіть функцію зі списку нижче⚙️',  reply_markup=markup)
        


        
        

        
@bot.message_handler(commands=["chatgpt"])
def botgpt(message):
 
       
         send = bot.send_message(message.chat.id, 'Введи інформацію для пошуку')
         bot.register_next_step_handler(send, chatgpt)
        
def chatgpt(message):
        import openai


        
        openai.api_key = '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'

        print(message.text)

        try:
                response = openai.Completion.create(
                            model = "text-davinci-003",
                            prompt= message.text,
                            temperature = 0.5,
                            max_tokens = 500,
                            top_p=1.0,
                            frequency_penalty=0.5,
                            presence_penalty=0.0,
                        )

                bot.send_message(message.chat.id, text=response['choices'][0]['text']) 
        except:
              time.sleep(10) //
              bot.send_message(message.chat.id, text= 'Зачекайте ще трохи...')
              chatgpt(message)
 

           
      
 
        

@bot.message_handler(content_types=["text"])

def handle_text(message):

    if message.text.strip() == 'Розклад 🗓' :
        markupS=types.ReplyKeyboardMarkup(True,False)
        
  
        markupS.row('Початок та кінець пар','Розклад занять')
        markupS.add('Повернутися до головного меню')

        bot.send_message(message.chat.id, text="Натисніть одну з кнопок ✅", reply_markup=markupS)
        

    elif message.text.strip() == 'Розклад занять' :
        markupA=types.ReplyKeyboardMarkup(True,False)

        markupA.row('КБ21015Б','КБ21016Б','КБ22014Б')
        markupA.add('Повернутися до головного меню')

        bot.send_message(message.chat.id, text="Вибери для продовження", reply_markup=markupA)

    elif message.text.strip() == 'Початок та кінець пар' :

        
        bot.send_message(message.chat.id, text="Актуальний розклад початку та кінця пар ⬇️")

        opTimeTable = open('static/pictures/timetable.png', 'rb')
        bot.send_photo(message.chat.id, opTimeTable)

       

    elif message.text.strip() == 'КБ21015Б':

            data = open('static\data\schedule\kb21015b.txt', 'r', encoding='utf-8')
            bot.send_message(message.chat.id, text= '           ㅤ   ' + data.read(),parse_mode='html')
            
    elif message.text.strip() == 'КБ21016Б':

            data = open('static\data\schedule\kb21016b.txt', 'r', encoding='utf-8')
            bot.send_message(message.chat.id, text= '           ㅤ   ' + data.read(),parse_mode='html')

    elif message.text.strip() == 'КБ22014Б':

            data = open('static\data\schedule\kb22014b.txt', 'r', encoding='utf-8')
            bot.send_message(message.chat.id, text= '           ㅤ   ' + data.read(),parse_mode='html')
            

    elif message.text.strip() == 'Бомбосховища⚠️' :

       opMap = open('static/pictures/map.png', 'rb')
       bot.send_photo(message.chat.id, opMap)
       
       bot.send_message(message.chat.id,"<b>🗒 Список бомбосховищ на території університету\n├ вул. Героїв Оборони, 14  (Корпус №5)\n├ вул. Героїв Оборони, 12В (Корпус №7)\n├ вул. Героїв Оборони, 11  (Корпус №10)\n├ вул. Героїв Оборони, 15  (Корпус №3)\n├ вул. Героїв Оборони, 17  (Корпус №2)\n└ вул. Родимцева, 19         (Корпус №1)\n </b>", parse_mode='html')

    elif message.text.strip() == 'Підтримка🛠' :

        bot.send_message(message.chat.id, text="З усіх технічних питань ---> @rokepump2 ")
        
 
    
    

    elif message.text.strip() == 'Новини університету📰':
            import os
            import numpy as np
            os.system('python3 news.py')
            
            addlist = np.load('ns.npy')


            markupV = types.InlineKeyboardMarkup()
            url_btn1 = types.InlineKeyboardButton(text=addlist[0],  url='https://nubip.edu.ua'  + addlist[1])
            url_btn2 = types.InlineKeyboardButton(text=addlist[2],  url='https://nubip.edu.ua'  + addlist[3])
            url_btn3 = types.InlineKeyboardButton(text=addlist[4],  url='https://nubip.edu.ua'  + addlist[5])
            url_btn4 = types.InlineKeyboardButton(text=addlist[6],  url='https://nubip.edu.ua'  + addlist[7])
            url_btn5 = types.InlineKeyboardButton(text=addlist[8],  url='https://nubip.edu.ua'  + addlist[9])
            url_btn6 = types.InlineKeyboardButton(text=addlist[10], url='https://nubip.edu.ua'  + addlist[11])
            url_btn7 = types.InlineKeyboardButton(text=addlist[12], url='https://nubip.edu.ua'  + addlist[13])
            url_btn8 = types.InlineKeyboardButton(text=addlist[14], url='https://nubip.edu.ua'  + addlist[15])
            url_btn9 = types.InlineKeyboardButton(text=addlist[16], url='https://nubip.edu.ua'  + addlist[17])
            url_btn10 = types.InlineKeyboardButton(text=addlist[18],url='https://nubip.edu.ua'  + addlist[19])
            markupV.add(url_btn1)
            markupV.add(url_btn2)
            markupV.add(url_btn3)
            markupV.add(url_btn4)
            markupV.add(url_btn5)
            markupV.add(url_btn6)
            markupV.add(url_btn7)
            markupV.add(url_btn8)
            markupV.add(url_btn9)
            markupV.add(url_btn10)

            from datetime import datetime

            current_datetime = datetime.now()
            
            bot.send_message(message.chat.id, 'Актуальні новини станом на '+ str(current_datetime.day) + '.' + str(current_datetime.month) + '.' +  str(current_datetime.year) + '⚠️', reply_markup=markupV)

            
            
    elif message.text.strip() == 'Повернутися до головного меню':
            
        markup=types.ReplyKeyboardMarkup(True,False)
        markup.row('Підтримка🛠','Розклад 🗓','Бомбосховища⚠️')
        markup.add('Новини університету📰')
        bot.send_message(message.chat.id, 'Виберіть пункт з меню',  reply_markup=markup)
            
    else:

       bot.send_message(message.chat.id,"Вибач, але я не розумію тебе😞")
       

              

bot.polling(none_stop=True, interval=0)

         



