from telegram.ext import *
from telegram import *

Token = '6647286471:AAHBzbIYyuvq3sqYB1cEtPkFgXpu9TFVqB8'

def start(update,context):
	update.message.reply_text(f"Hii {update.effective_user.full_name}")


updater = Updater(token = Token,use_context= True)

ds = updater.dispatcher

ds.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
