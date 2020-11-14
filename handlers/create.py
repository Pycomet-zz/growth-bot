from config import *
from functions import register_session

markup = types.ForceReply(selective=False)

client = ""
phone = ""

@bot.message_handler(commands=['create', 'add'])
def create(msg):
    """
    Add A New Session String
    """

    if msg.from_user.id in ADMINS:
        bot.reply_to(
            msg,
            f"✍️ Creating a new session string for the Weblulue Growth Tool..... "
        )

        question = bot.send_message(
            msg.from_user.id,
            "Please insert your phone number (e.g 1234423234 excluding the '+' sign)? ..",
            reply_markup=markup
        )
        bot.register_next_step_handler(question, generate_session)

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                use_aliases=True
                )
        )


def generate_session(msg):
    """
    Generates The New Session With Phone Number
    """

    global client 
    global phone
    phone = msg.text

    loop = asyncio.new_event_loop()

    client = TelegramClient(StringSession(), API_ID, API_HASH, loop=loop)

    client.loop.run_until_complete(client.connect())

    authorized = client.loop.run_until_complete(client.is_user_authorized())

    if authorized == False:
        ask = client.loop.run_until_complete(
            client.send_code_request(
                phone = msg.text,
            )
        )


        question = bot.send_message(
            msg.from_user.id,
            f"What is the code you received?",
            reply_markup=markup
        )

        me = client.sign_in(phone_number, input('Enter code: '))

        bot.register_next_step_handler(question, get_code)

        return client, phone




def get_code(msg):
    "Registers The Authentication Code"

    code = msg.text
    
    try:
        client.loop.run_until_complete(
            client.sign_in(
                phone = phone,
                code = code
            )
        )

        user = client.loop.run_until_complete(client.get_me())

        string = client.loop.run_until_complete(client.session.save())

        result = register_session(
            user = user,
            string = string
        )

        bot.send_message(
            msg.from_user.id,
            "You have successfully added {result} session - {string} to the database"
        )


    except Exception as e:

        bot.send_message(
            msg.from_user.id,
            "Oooppss 🥺, you have to try again! You probably got the code wrong"
        )

        create(msg)