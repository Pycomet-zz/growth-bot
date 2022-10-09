from config import *
from handlers import *


def lister(msg):
    [print(x) for x in msg]


@server.route('/' + TOKEN, methods=['POST', 'GET'])
def checkWebhook():
    # bot.set_update_listener(lister)
    # bot.infinite_polling()
    # bot.process_new_updates(
    #     [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
    return "Your bot application is still active!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL + '/' + TOKEN)

    return "Application running!", 200


if __name__ == "__main__":

    if DEBUG == False:
        server.run()
    else:
        bot.remove_webhook()
        print("Bot running")
        bot.polling(none_stop=True)
