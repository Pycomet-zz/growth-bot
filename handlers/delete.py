from config import *


@bot.message_handler(commands=["delete"])
def delete(msg):
    """Deleting Session Files"""
    if msg.from_user.id in ADMINS:
        question = bot.send_message(
            msg.from_user.id,
            "What is the phone number attached to the session you wish to delete?",
        )

        bot.register_next_step_handler(question, delete_session)


def delete_session(msg):
    """
    Querying the mongo atlas database
    """
    phone = msg.text

    criteria = {"Phone": phone}

    try:
        result = db.sessions.delete_one(criteria)

        bot.send_message(
            msg.from_user.id, f"Deleted {result.deleted_count} Successfully!"
        )

    except:
        bot.send_message(msg.from_user.id, f"Failed to find session!")
