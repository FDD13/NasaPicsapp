import random
import telegram
import logging
import os
import time
import argparse
from dotenv import load_dotenv
from fetch_image_helpers import get_pictures



def take_paths(directory):
    filesindirs = os.listdir(directory)
    random.shuffle(filesindirs)
    picture_paths = []
    for filesindir in filesindirs:
        file = os.path.join(str(directory), filesindir)
        picture_paths.append(file)
    return picture_paths



def main():
    load_dotenv()
    token = os.getenv("TG_TOKEN")
    bot = telegram.Bot(token=token)
    tg_chat_id = os.getenv("TG_CHAT_ID")
    pics_interval = 14400


    parser = argparse.ArgumentParser(description='Программа для скачивания картинок в директории')
    parser.add_argument('directory', help="Введите адрес директории: ")
    args = parser.parse_args()


    while True:
        picture_packet = take_paths(args.directory)
        for picture in picture_packet:
            bot.send_message(chat_id=tg_chat_id, text="Hello. Today's photos:")
            with open(picture, 'rb') as photo:
                bot.send_photo(chat_id=tg_chat_id, photo=photo)
            time.sleep(pics_interval)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Завершение работы скрипта')