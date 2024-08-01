import random
import telegram
import logging
import os
import time
import argparse
from dotenv import load_dotenv
from fetch_image_helpers import get_pictures


def take_file(directory):
    filesindirs = os.listdir(directory)
    random.shuffle(filesindirs)
    for filesindir in filesindirs:
        file = os.path.join(str(directory), filesindir)
    return file


def time_in_seconds(hours):
    seconds = hours * 3600
    time.sleep(seconds)


def main():
    load_dotenv()
    token = os.getenv("TG_TOKEN")
    bot = telegram.Bot(token=token)
    tg_chat_id = os.getenv("TG_CHAT_ID")
    hours = 4

    parser = argparse.ArgumentParser(description='Программа для скачивания картинок в директории')
    parser.add_argument('directory', help="Введите адрес директории: ")
    args = parser.parse_args()


    while True:
        pictures = take_file(args.directory)
        with open(pictures, 'rb') as photo:
            bot.send_message(chat_id=tg_chat_id, text="Hello. Today's photos:")
            bot.send_photo(chat_id=tg_chat_id, photo=photo)
        timer = time_in_seconds(hours)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Завершение работы скрипта')