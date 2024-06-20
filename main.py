import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from helpers import get_pictures


import telegram
import logging
import os
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from helpers import get_pictures





def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")



def picture(update: Update, context: CallbackContext):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('D:\FD Python\\nasawork\\NASA EPIC images\\image_4.png', 'rb'))



def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    bot = telegram.Bot(token=token)
    pictures = os.path


    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


    picture_handler = MessageHandler(Filters.photo & (~Filters.command), picture)
    dispatcher.add_handler(picture_handler)

    updater.start_polling()





if __name__ == '__main__':
    main()