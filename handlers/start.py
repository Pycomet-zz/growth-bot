from config import *
from functions import add_users, deactivate_session, fetch_sessions

group = ""


@bot.message_handler(commands=["start", "Start"])
def startbot(msg):
    """
    Starting The Bot Dialog
    """
    if msg.from_user.id in ADMINS:
        bot.reply_to(
            msg,
            emoji.emojize(
                f":smile: Welcome back {msg.from_user.first_name}", language="alias"
            ),
        )

        start_process(user=msg.from_user)

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                language="alias",
            ),
        )


def start_process(user):
    "Step One To Running The Bot"
    question = bot.send_message(
        user.id,
        emoji.emojize(
            "Where would you want today's group target to be? :speedboat: (use format - t.me/groupname)",
            language="alias",
        ),
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
            emoji.emojize("Where do you want to start? :speedboat: ", language="alias"),
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
            "Awesome! The Hunters Growth Tool Is Starting :rocket:", language="alias"
        ),
    )

    # # Target group admins
    # admin_ids = [user.user.id for user in bot.get_chat_administrators(group)]
    # for session, user in zip(SESSIONS, SESSION_USERS):
    session_data = fetch_sessions()

    # import pdb
    # pdb.set_trace()
    for (user, session) in session_data:

        message = bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                f":rocket: {user} just added 0 new users to the group with 0 failed attempts",
                language="alias",
            ),
            parse_mode="html",
        )
        message_id = message.message_id
        chat_id = message.chat.id
        print(chat_id)

        # Igniting the client instance
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        client = TelegramClient(
            StringSession(session), API_ID, API_HASH, loop=loop
        ).start()

        record = client.loop.run_until_complete(
            add_users(
                bot=bot,
                client=client,
                target=group,
                start=index,
                message_id=message_id,
                runner=user,
            )
        )

        index += 50

        client.disconnect()

        if record == "Done":

            bot.send_message(
                msg.from_user.id,
                emoji.emojize(
                    f":rocket: Weblulue Support is done adding from this group.",
                    language="alias",
                ),
            )
            break

        else:

            bot.send_message(
                msg.from_user.id,
                emoji.emojize(
                    f"Done with this {user} client. Switching Gears Now !! :rocket:",
                    language="alias",
                ),
            )
            deactivate_session(session=session)
