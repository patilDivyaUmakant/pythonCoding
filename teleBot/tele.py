from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import requests 
api_key = '5082977317:AAF11kdDpSFXSYj-j-LrAoluPnwyC_1RA1Y'
updater = Updater(token = api_key, use_context = True)
dispatcher = updater.dispatcher
updater.start_polling()



greetings= ["hello","hi","hey"]
def hello(update,context) : 
    context.bot.send_message(chat_id = update.effective_chat.id,text = "hello, how are you")

hello_handler = CommandHandler(greetings,hello)   
dispatcher.add_handler(hello_handler)



def speedMotion(update,context) : 
    context.bot.send_message(chat_id = update.effective_chat.id,text = "https://youtu.be/S9Z1a3sZfHY")

video_handler = CommandHandler("speed",speedMotion)   
dispatcher.add_handler(video_handler)


def summary(update , context) :
    response = requests.get("https://api.covid19api.com/summary")
    if response.status_code == 200 :
        data = response.json()
        # print (data)
        print (data["Date"][0:10])
        date = data["Date"][0:10]
        result = f"Covid-19 summary - {date} \n"
        print (data["Global"])
        for att,value in data["Global"].items() : 
          if att not in ["NewRecovered","TotalRecovered","Date"] : 
            print (att, value)
            result += att +":"+ str(value) + "\n"
        context.bot.send_message(chat_id = update.effective_chat.id,text = result)
    else :
        context.bot.send_message(chat_id = update.effective_chat.id,text = "Something went wrong on Server!! ")  

summary_handler = CommandHandler("summary",summary)
dispatcher.add_handler(summary_handler)

def unknown(update,context) :
    context.bot.send_message(chat_id = update.effective_chat.id,text = "Sorry, I didn't understand!! ")

unknown_handler = MessageHandler(Filters.command,unknown)
dispatcher.add_handler(unknown_handler)
updater.idle()