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
    bot.set_webhook(url=SERVER_URL + '/' + TOKEN)
    logger.info(f"New webhook url set {SERVER_URL}/{TOKEN}")

    return {
        "status": "LIVE"
    }


@app.post(f'/{TOKEN}/')
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


# bot.delete_webhook()

# bot.infinity_polling()

# if __name__ == "__main__":
#     if DEBUG == False:
#         server.run()
#     else:
#         bot.remove_webhook()
#         print("Bot running")
#         bot.polling(none_stop=True)


@bot.message_handler(commands=['start', 'Start'])
def startbot(msg):
    """
    Starting The Bot Dialog
    """
    if msg.from_user.id in ADMINS:
        bot.reply_to(
            msg,
            emoji.emojize(
                f":smile: Welcome back {msg.from_user.first_name}",
                language='alias'
            )
        )

        start_process(user=msg.from_user)

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                language='alias'
            )
        )
