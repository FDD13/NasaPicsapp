import random
import telegram
import logging
import os
import time
import argparse
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from helpers import get_pictures


def take_files(directory):
    global file
    filesindirs = os.listdir(directory)
    random.shuffle(filesindirs)
    for filesindir in filesindirs:
        path = os.path.join(str(filesindir))
        file = os.path.join(str(directory), path)
    return file



def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    bot = telegram.Bot(token=token)


    parser = argparse.ArgumentParser(description='Программа для скачивания картинок в директории')
    parser.add_argument('directory', help="Введите адрес директории: ")
    args = parser.parse_args()


    while True:
        pictures = take_files(args.directory)
        bot.send_message(chat_id=39444986, text="Hello. Today's photos:")
        bot.send_photo(chat_id=39444986, photo=open(pictures, 'rb'))
        time.sleep(14400)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Завершение работы скрипта')