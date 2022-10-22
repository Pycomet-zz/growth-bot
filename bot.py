from config import *
from handlers import *


# def lister(msg):
#     [print(x) for x in msg]


# @server.route('/' + TOKEN, methods=['POST'])
# def checkWebhook():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "Your bot application is still active!", 200


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url=SERVER_URL + '/' + TOKEN)
#     return "Application running!", 200


@app.get("/")
def pong():

    # bot.delete_webhook()

    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL + "/" + TOKEN)
    logger.info(f"New webhook url set {SERVER_URL}/{TOKEN}")

    return {"status": "LIVE"}


@app.post(f"/{TOKEN}/")
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


webhook_info = bot.get_webhook_info()
if webhook_info.url:
    bot.delete_webhook()

bot.infinity_polling()

# if __name__ == "__main__":
#     if DEBUG == False:
#         server.run()
#     else:
#         bot.remove_webhook()
#         print("Bot running")
#         bot.polling(none_stop=True)
