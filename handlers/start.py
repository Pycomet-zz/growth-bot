from config import *
from functions import add_users

group = ""

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
                use_aliases=True
                )
        )

        start_process(user=msg.from_user)

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                use_aliases=True
                )
        )


def start_process(user):
    "Step One To Running The Bot"
    question = bot.send_message(
        user.id,
        emoji.emojize(
            "Where would you want today's group target to be? :speedboat: (use format - t.me/groupname)",
            use_aliases=True
        )
    )

    bot.register_next_step_handler(question, joinGroup)


def joinGroup(msg):
    """Join The Target Group And Request Message From User"""

    global group

    try:
        group = msg.text   

        # Ask Request
        question = bot.reply_to(
            msg,
            emoji.emojize(
                "Where do you want to start? :speedboat: ",
                use_aliases=True
            )
        )
        bot.register_next_step_handler(question, startTool)   

    except Exception as e:

        bot.send_message(msg.from_user.id, f"Ooops! - {e}")


def startTool(msg):
    """Start the tool with the index starting point defined"""
    index = int(msg.text)

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            "Awesome! The Hunters Growth Tool Is Starting :rocket:",
            use_aliases=True
        )
    )

    # Collect all Session Strings
    # SESSIONS = [sessions[i]['SessionString'] for i in range(sessions.count())]
    # SESSION_USERS = [sessions[i]['first_name'] for i in range(sessions.count())]
    # NEW VERSION SESSION STRINGS
    SESSIONS = [
        '1AZWarzQBu5dHKdZmSY6Sj8Bmn5hkCHCY5Ty_BHmG5PspeTrRIdXTt2Lafgdw1PQnjQDPTmcEcD5gWMhVzjdHzDPESMmJu1ErvvDRXv6JMcz_X-7q6OjqKlaJagrIghocLsm1VLHzOm2qkKbGRvGrXxKMMiJarjqmGHP17aAoYJ1gjXrv6v0WEeDhaYgpmmtVjr2YCS8hpUg64bUmow0j4vn4MzPtC6Qz5gMy_7iRplHycUdR73S_p7PIuEltzn5h51Hb8Lg5mvIjaenkuacVYGtWbXk0l1qDuaid823EVvoZkNuTzeX9FoGFUXRhV4WkcTGN4WC9pidSSDD9rnc6FV7JjvtwrHk=',
        '1AZWarzQBu3XiqxzZCLgUdB6cshQ-IAVQHDaLo9v6Mg-VgfnXw0ZLmDgB9v0bzoMlc0LqZKjuohJOhm2nC9SDx0Ht3tOqOHbsGWPpmxwLU_iTg3rUG-_8a3rU6VphR9r5rTapmyxwPa9p81D13Bk5SeMGtRtgGM7m_3aybD4MCuk5ArTyMXM7I8WB5z2hrFYGbFO5Iwbg5Qp-sL9YM9mauaw-1TBbx1Jf26zmlNtUKu6kXr2sE2KJzP61lIGnFu--p2229YZigA1WTf7IzeZ5vQmdc1nmD1xUpS9hT8jYGIm9TfMfkKmprV83H4lQaMt3XRxkdGvCgEDnAC0OMRCsnHBRkA7ljNs=',
    ]
    SESSION_USERS = [
        'Client 1',
        'Client 2',
    ]

    # # Target group admins
    # admin_ids = [user.user.id for user in bot.get_chat_administrators(group)]
    for session, user in zip(SESSIONS, SESSION_USERS):

        message = bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                f":rocket: {user} just added 0 new users to the group with 0 failed attempts",
                use_aliases=True
            ),
            parse_mode="html"
        )
        message_id = message.message_id
        chat_id = message.chat.id
        print(chat_id)
        
        # Igniting the client instance
        loop = asyncio.new_event_loop()
        client = TelegramClient(
            StringSession(session),
            API_ID,
            API_HASH,
            loop = loop
        ).start()


        record = client.loop.run_until_complete(
            add_users(
            bot = bot,
            client = client,
            target = group,
            start = index,
            message_id = message_id,
            runner = user
            )
        )
        
        client.disconnect()


        if record == "Done":

            bot.send_message(
                msg.from_user.id,
                emoji.emojize(
                    f":rocket: Weblulue Support is done adding from this group.",
                    use_aliases=True
                )
            )
            break


        else:

            bot.send_message(
                msg.from_user.id,
                emoji.emojize(
                    f"Done with this {user} client. Switching Gears Now !! :rocket:",
                    use_aliases=True
                )
            )
            time.sleep(5)
