from dotenv import load_dotenv
import os
#from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
#from telegram.constants import ParseMode


load_dotenv(dotenv_path="creds.env")

api_key = os.getenv("API_KEY")
