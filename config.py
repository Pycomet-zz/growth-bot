import os
from decouple import config
import time
import random
## BOT CONFIGURATION
from flask import Flask, request
import telebot
from telebot import types
import emoji
from pymongo import MongoClient
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import AddContactRequest, ImportContactsRequest, DeleteContactsRequest

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


DEBUG = True

GROUP = config("GROUP")


API_ID = config("API_ID")
API_HASH = config("API_HASH")

# if SESSIONS is not None:
#     try:
#         SESSIONS_LIST = [i for i in SESSIONS.split(',')]
#     except:
#         SESSIONS_LIST = SESSIONS


TOKEN = config("TOKEN")

SERVER_URL = config("SERVER_URL")

ADMINS = [config("ADMIN1")]

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

 