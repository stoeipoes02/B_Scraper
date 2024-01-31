from dotenv import load_dotenv
import os

import telegram
from telegram.constants import ParseMode
#from telegram.ext import Updater, MessageHandler, filters, CommandHandler

# Load Key
load_dotenv(dotenv_path="creds.env")
api_key = os.getenv("API_KEY")

bot = telegram.Bot(api_key)


import asyncio
# asyncio.run(bot.send_message(chat_id=-4150084167, text='<b>hallo</b>', parse_mode=ParseMode.HTML))

with open('Yggdrasil.png', 'rb') as picture:
    asyncio.run(bot.send_photo(chat_id=-4150084167, photo=picture, caption='<b>Foto</b>',parse_mode=ParseMode.HTML))