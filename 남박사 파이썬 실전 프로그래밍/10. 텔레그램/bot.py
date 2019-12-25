import telepot

TELEGRAM_TOKEN = "1005159877:AAG-JbJX2OqeTuY7X_EQryzE7Tjq-QPa8vw"

def handler(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)

    if content_type == "text":
        bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))

bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)