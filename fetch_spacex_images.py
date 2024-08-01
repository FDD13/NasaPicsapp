import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import get_pictures


def fetch_spacex_id_launch(url: list, demo_key: str, id: str):
    images_path = 'Space X images'
    payloads = {
        'api_key': f'{demo_key}',
        'id': id
    }
    response = requests.get(url, params=payloads)
    data = json.loads(response.text)
    spacex_urls = data['links']['flickr']['original']
    spacex_pics = get_pictures(spacex_urls, images_path=images_path, params=payloads)


def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания Space X картинок")
    parser.add_argument("-id", "--flight_id", default=None, help="Введите ID картинок Space X: ")
    args = parser.parse_args()


    load_dotenv()
    demo_key = os.getenv("NASA_API_KEY")
    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.flight_id}'
    if args.flight_id:
        spacex_pics = fetch_spacex_id_launch(spacex_url, demo_key, args.flight_id)
    else:
        print("Картинки с последнего полета Space X еще не доступны")


if __name__ == '__main__':
    main()
