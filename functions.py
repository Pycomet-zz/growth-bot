import string
from config import *
from telethon.tl.types import PeerChat
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import (
    UserPrivacyRestrictedError,
    PeerFloodError,
    UserNotMutualContactError,
    UserChannelsTooMuchError,
)


def check_user(user):
    "This checks to see that the use entity meets all the criteria before being added"

    if user.bot == False:
        if user.deleted != True:
            if user.last_name is None:
                user.last_name = ""
            else:
                pass

            if str(user.status) == "UserStatusRecently()":
                if user.phone is None and user.username is None:
                    user.phone = ""
                    user.username = ""
                elif user.phone is None and user.username is not None:
                    user.phone = ""
                elif user.phone is not None and user.username is None:
                    user.username = ""
                else:
                    pass
                return user
            else:
                return None
        else:
            return None
    else:
        return None


async def join_group(client, group):
    "Joining A Specific Group"
    join = await client(JoinChannelRequest(group))
    return join


async def add_users(bot, client, target, start, message_id, runner):
    """
    Function To Carry Out Adding Process
    """
    added = 0
    stopped = 0
    contacts = 0

    condition = True

    while condition:

        offset = 0
        group = await client.get_entity(GROUP)

        await join_group(client=client, group=group)

        async for member in client.iter_participants(target):

            if start > offset:
                offset += 1
                pass

            else:
                user = check_user(user=member)

                if user:
                    try:
                        # Second, Add User To Group
                        await client(InviteToChannelRequest(group, [member]))

                        added += 1

                        # update count
                        bot.edit_message_text(
                            chat_id=ADMINS[0],
                            message_id=message_id,
                            text=emoji.emojize(
                                f"<b>:rocket: {runner} added {added} new users to the group. And has {stopped} failed attempts</b>",
                                language="alias",
                            ),
                            parse_mode="html",
                        )
                        time.sleep(random.choice(range(3, 5)))

                    except UserPrivacyRestrictedError:
                        pass
                    except UserChannelsTooMuchError:
                        pass
                    except UserNotMutualContactError:
                        pass

                    except PeerFloodError as e:

                        stopped += 1

                        bot.edit_message_text(
                            chat_id=ADMINS[0],
                            message_id=message_id,
                            text=emoji.emojize(
                                f"<b>:rocket: {runner} added {added} new users to the group, with {stopped} failed attempts. Cooling Down For 30 seconds!!!</b>",
                                language="alias",
                            ),
                            parse_mode="html",
                        )

                        time.sleep(30)

                        if stopped == 5:
                            condition = False
                            return added

                    except Exception as e:
                        stopped += 1
                        pass

        # After adding All The Users
        condition = False
        return "Done"


def fetch_sessions() -> list:
    "Get All (Name, Session) from Db"
    response = client["tool_database"]["sessions"].find({})
    data = [
        (each["FirstName"], each["SessionString"])
        for each in response
        if each["Active"] == True
    ]
    return data


def deactivate_session(session: str) -> bool:
    "Sets The Active Property To 'False'"
    res = client["tool_database"]["sessions"].find_one(
        {"SessionString": session})

    if res != None:
        client["tool_database"]["sessions"].update_one(
            {"SessionString": session}, {"$set": {"Active": False}}
        )
        print("Session deactivated!")
        return True
    else:
        return False


def activate_all_sessions():
    "Updates all sessions to active state"
    res = client["tool_database"]["sessions"].find({})
    count = 0
    for session in res:
        count += 1
        client["tool_database"]["sessions"].update_one(
            {"SessionString": session}, {"$set": {"Active": True}}
        )
        print("Session activated!")
    return True, count


def add_session(user, string) -> str:
    "Adding A New Session String To The Database"
    # Send Session To DB
    post_data = {
        "id": user.id,
        "Owner": user.username,
        "FirstName": user.first_name,
        "Phone": user.phone,
        "SessionString": string,
        "AccessHash": user.access_hash,
        "Active": True,
    }
    result = client["tool_database"]["sessions"].insert_one(post_data)
    return result._id
