from config import *
from functions import add_session

markup = types.ForceReply(selective=False)

client = ""
phone = ""
code = ""


@bot.message_handler(commands=["create", "add"])
def create(msg):
    """
    Add A New Session String
    """

    if msg.from_user.id in ADMINS:
        bot.reply_to(
            msg, f"✍️ Creating a new session string for the Weblulue Growth Tool..... "
        )

        question = bot.send_message(
            msg.from_user.id,
            "Please insert your phone number (e.g 1234423234 excluding the '+' sign)? ..",
            reply_markup=markup,
        )
        bot.register_next_step_handler(question, generate_session)

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                language="alias",
            ),
        )


def generate_session(msg):
    """
    Generates The New Session With Phone Number
    """

    global client
    global phone
    phone = msg.text

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = TelegramClient(StringSession(""), API_ID, API_HASH, loop=loop).start(
        phone=phone,
        force_sms=True,
        code_callback=input("Enter code ?"),
    )

    user = client.loop.run_until_complete(client.get_me())

    string = client.loop.run_until_complete(client.session.save())

    result = add_session(user=user, string=string)

    bot.send_message(
        msg.from_user.id,
        f"You have successfully added {result} session - {string} to the database",
    )

    # authorized = client.loop.run_until_complete(client.is_user_authorized())

    # if authorized == False:
    #     ask = client.loop.run_until_complete(
    #         client.send_code_request(
    #             phone=msg.text,
    #         )
    #     )

    #     question = bot.send_message(
    #         msg.from_user.id,
    #         f"What is the code you received?",
    #         reply_markup=markup
    #     )

    #     me = client.sign_in(phone_number, input('Enter code: '))

    #     bot.register_next_step_handler(question, get_code)

    #     return client, phone


def code_callback(msg):

    global code
    while code == "":

        question = bot.send_message(
            msg.from_user.id, f"What is the code you received?", reply_markup=markup
        )
        bot.register_next_step_handler(question, get_code)


def get_code(msg):
    "Registers The Authentication Code"
    global code

    code = msg.text
    return code

    try:
        client.loop.run_until_complete(client.sign_in(phone=phone, code=code))

        user = client.loop.run_until_complete(client.get_me())

        string = client.loop.run_until_complete(client.session.save())

        result = add_session(user=user, string=string)

        bot.send_message(
            msg.from_user.id,
            "You have successfully added {result} session - {string} to the database",
        )

    except Exception as e:

        bot.send_message(
            msg.from_user.id,
            "Oooppss 🥺, you have to try again! You probably got the code wrong",
        )

        create(msg)
