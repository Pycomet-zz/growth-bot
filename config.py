import logging
import os
from decouple import config
import time
import random

# BOT CONFIGURATION
from fastapi import FastAPI, Depends
import telebot
from telebot import types
import emoji
from pymongo import MongoClient
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import (
    AddContactRequest,
    ImportContactsRequest,
    DeleteContactsRequest,
)

import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

DEBUG = True

GROUP = config("GROUP")


client = MongoClient(config("MONGO_URI"))


API_ID = config("API_ID")
API_HASH = config("API_HASH")

# if SESSIONS is not None:
#     try:
#         SESSIONS_LIST = [i for i in SESSIONS.split(',')]
#     except:
#         SESSIONS_LIST = SESSIONS


TOKEN = config("TOKEN")

SERVER_URL = config("SERVER_URL")

ADMINS = [int(config("ADMIN"))]

bot = telebot.TeleBot(TOKEN)
app = FastAPI(docs=None, redoc_url=None)
