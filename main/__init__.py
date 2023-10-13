# Github.com/Vasusen-code

import logging
import sys
import time

from decouple import config
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

# variables
API_ID = "29849415"
API_HASH = "0dd6c10897b85d7f10a8dcdeb74f8b8a"
BOT_TOKEN = "6471855948:AAGMgs0adsUdHvffmhx3sXkhgQA9hlxEA7k"
SESSION = "BQDAM7MAxsDeSpTb2x241UMMYa0BwX-bwqUg0tCfBdn-ZPcAUv_p2DvpFXuCwqI1O8ZTi7pQSSf8xcI1mdMTYEFg6M_crN7Z1CUHIBrpt-A45MM3NJnnLJ58WGG99IabAyAacTZPGFCQgL7CV95JMYb7g1IHFTbA_2nT_pyOHN-bQuejB9sUeRQC7b2mnZA7H9m4fwoEOFxyZ8_ZJ1L5p1QImew8EuD-w107kB0OBm20dhLU0KL-Y0C6reBRyjN7V1Vz0Rmpssq4phrApimnuDxr8NTt3D32XeXlBG-WCARlyptG0UrdXLVFMZeIKJSg6wJdrMyj5Qj07uc_lavUwBTY1ranfQAAAAGIyLuQAA"
FORCESUB = "S_Hindi_Movie"
AUTH = "5165943027"

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client(session_name=SESSION, api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted", bot_token=BOT_TOKEN, api_id=int(API_ID), api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
