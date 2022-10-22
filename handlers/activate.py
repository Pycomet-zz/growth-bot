from config import *
from functions import activate_all_sessions


@bot.message_handler(commands=["activateall"])
def activate(msg):
    """The Function Activate All The Session Accs"""
    if msg.from_user.id in ADMINS:

        status, count = activate_all_sessions()

        if status == True:
            bot.reply_to(
                msg,
                emoji.emojize(
                    f":smile: Welcome back {msg.from_user.first_name}, All ({count}) Sessions Have Been Activated!",
                    language="alias",
                ),
            )
        else:
            bot.reply_to(
                msg,
                emoji.emojize(
                    f":sad: Activation Failed, An Error Occurred!", language="alias"
                ),
            )

    else:
        bot.reply_to(
            msg,
            emoji.emojize(
                ":warning: Sorry but you are not allowed to use this tool. Contact @codefred to get started.",
                language="alias",
            ),
        )
