#import librarys that we well use
import telebot
import requests
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
    
    txt = message.text
    
    #if message value >= 1 and <=604
    if int(txt) >= 1 and int(txt) <= 604:
        image_name = f'{txt}.png'
        img_data = requests.get(f"https://quran.ksu.edu.sa/tajweed_png/{txt}.png").content
        with open(image_name, 'wb') as handler:
            handler.write(img_data)
            
        #if message value >= 1 and <=9
        if int(txt) >= 1 and int(txt)<=9:
            mp3_name = f'{txt}.mp3'
            mp3_data = requests.get(f"https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة 00{txt}(MP3_128K).mp3").content
            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data)

        #if message value >= 10 and <=99        
        if int(txt) >= 10 and int(txt)<=99:
            mp3_name = f'{txt}.mp3'
            mp3_data = requests.get("https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة 0"+txt+"(MP3_128K).mp3" ).content
            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data)
                
        #if message value >= 100 and <=604       
        if int(txt) >= 100 and int(txt)<=604:
            mp3_name = f'{txt}.mp3'
            mp3_data = "https://ia801803.us.archive.org/10/items/1-mp-3-128-k/ألقران الكريم - أيمن سويد الصفحة "+txt+"(MP3_128K).mp3" 
            with open(mp3_name, 'wb') as handler:
                handler.write(mp3_data)
                
        #sending page photo and audio
        bot.send_photo(message.chat.id,open(image_name,"rb") , caption=f"page number : {txt}")
        bot.send_audio(message.chat.id,open(mp3_name,"rb") , caption=f"page number : {txt}")
        
        #removeing page photo and audio from storage 
        os.remove(image_name)
        os.remove(mp3_name)

    #if value is not true
    else:
        str(txt)
        bot.send_message(message.chat.id , "wrong page number")
bot.polling()