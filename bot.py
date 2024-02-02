from dotenv import load_dotenv
import os

import telegram
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, Updater, MessageHandler, CommandHandler, filters, ContextTypes

import asyncio


# Load Key
load_dotenv(dotenv_path="creds.env")
TOKEN = os.getenv("API_KEY")
USERNAME = "Scrappy_Scraper_Bot"

bot = telegram.Bot(token=TOKEN)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hey i am a banana')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a banana, please type something so i can respond')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('THis is a custom command')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in text:
        return 'hey'
    if 'how' in text:
        return 'Nibbas'
    return 'i do not understand you..'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if USERNAME in text:
            new_text: str = text.replace(USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause erorr {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)