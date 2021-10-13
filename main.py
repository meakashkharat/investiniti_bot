from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json', verify=False).json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def start(update, context):
    url = "Hello Welcome to Investinity Swing Predication"
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=url)

def getTarget(update, context):
    try : 
        url = "Hello Welcome to Investinity Swing Predication"
        price = float(context.args[0])
        per = float(context.args[1])
        sl=price - (price*per/100)
        target = price + (price*per/100)
        message ="Target = "+str(target) +" SL = "+str(sl)
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text=message)
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def calculateTarget(update, context):
    url = "Hello Welcome to Investinity Swing Predication"
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=url)

def getce(update, context):
    ce = int(context.args[0])
    price = int(context.args[1])
    url = "{} CE buy above {}, SL {}, first target {}, second target {}, third target {}, rest open".format(ce,price,price-10,price+30,price+60,price+100),
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=url)

def getpe(update, context):
    ce = int(context.args[0])
    price = int(context.args[1])
    url = '{} PE buy above {}, SL {}, first target {}, second target {}, third target {}, rest open'.format(ce,price,price-10,price+30,price+60,price+100),
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=url)


def sendFile(update, context):
    url = "Hello Welcome to Investinity Swing Predication"
    chat_id = update.message.chat_id
    context.bot.send_document(chat_id=chat_id, document=open('allgrades.xlsx','rb'))

def getpartial(update, context):
    ce = float(context.args[0])
    price = int(context.args[1])
    url = '{} PE buy above {}, SL {}, first target {}, second target {}, third target {}, rest open'.format(ce,price,price-10,price+30,price+60,price+100),
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=url)

def main():
    updater = Updater('1817219841:AAF2eo2mh99GevkI4l2B_Rqyzf5-jHt2iwM', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('gettheexcel',sendFile))
    dp.add_handler(CommandHandler('target',getTarget))
    dp.add_handler(CommandHandler('ce',getce))
    dp.add_handler(CommandHandler('pe',getpe))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
