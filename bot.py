from dotenv import load_dotenv
import os

import telegram
#from telegram.ext import Updater, MessageHandler, filters, CommandHandler

# Load Key
load_dotenv(dotenv_path="creds.env")
api_key = os.getenv("API_KEY")

bot = telegram.Bot(api_key)


import asyncio
asyncio.run(bot.send_message(-4150084167, 'hey'))