import telebot


api_key = "6647286471:AAHBzbIYyuvq3sqYB1cEtPkFgXpu9TFVqB8"

Bot = telebot.TeleBot(api_key)

print("Bot Started...")


@Bot.message_handler(commands = ['start'])
def send_start_command(msg):
  Bot.send_message(msg.chat.id,"Dora Puaa")
  

@Bot.message_handler(func = lambda  msg: msg.text == msg.text)
def send_prink(msg):
  Bot.send_message(msg.chat.id,"Dora Puaa")
  Bot.send_photo(msg.chat.id,open('rohan_dora_photo.jpg','rb'))

Bot.polling()
