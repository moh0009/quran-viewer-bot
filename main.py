#import librarys that we well use
import telebot
import requests as re
import os
#token
g = os.environ['g']
#Initializing bot
bot = telebot.TeleBot(g)
#when user send /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"""hello
                   ------------------
    this is quran viewer bot
------------------                   
send page number 
and i well send to you a page photo and audio""")
#when user send page number
@bot.message_handler()
def page_num(message):
    text = message.text
    id = message.chat.id
    if text.isdigit() == True:
        
        if int(text) <= 604 and int(text)>=1:
            
            img_name = f"{text}.png"
            img_data = re.get(f"https://image.slidesharecdn.com/random-160202103353/95/-{text}-1024.jpg").content

            with open(img_name, 'wb') as handler:
                handler.write(img_data) 

            bot.send_photo(id,open(img_name,"rb") , caption=f"page number : {text}")
            os.remove(img_name)

        if int(text) <= 9 and int(text)>=1:
            
            mp3_name = f"{text}.mp3"
            mp3_data = re.get(f"https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة 00{text}(MP3_128K).mp3").content

            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data) 

            bot.send_audio(id,open(mp3_name,"rb") , caption=f"page number : {text}")
            os.remove(mp3_name)

        if int(text) <= 99 and int(text)>=10:
            
            mp3_name = f"{text}.mp3"
            mp3_data = re.get(f"https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة 0{text}(MP3_128K).mp3").content

            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data) 

            bot.send_audio(id,open(mp3_name,"rb") , caption=f"page number : {text}")
            os.remove(mp3_name)

        if int(text) <= 604 and int(text)>=100:
            
            mp3_name = f"{text}.mp3"
            mp3_data = re.get(f"https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة {text}(MP3_128K).mp3").content

            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data) 

            bot.send_audio(id,open(mp3_name,"rb") , caption=f"page number : {text}")
            os.remove(mp3_name)

        else:
            bot.send_message(id,"wrong page number")
    else:
        bot.send_message(id,"wrong page type")
bot.polling()