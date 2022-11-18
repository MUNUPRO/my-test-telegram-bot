from telegram.ext import *
from telegram import *

Token = '5676375736:AAErAYZ_tcBBp_Ya2pJpfnYZ6382e310NFw'

def start(update,context):
	update.message.reply_text(f"Hii {update.effective_user.full_name}")


updater = Updater(token = Token,use_context= True)

ds = updater.dispatcher

ds.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()