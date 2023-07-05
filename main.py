from telegram.ext import *
from telegram import *

Token = '6152413141:AAGVnf-4l2WnRce8Q68KUtAK_JOELxc_BO8'

def start(update,context):
	update.message.reply_text(f"Hii {update.effective_user.full_name}")


updater = Updater(token = Token,use_context= True)

ds = updater.dispatcher

ds.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
