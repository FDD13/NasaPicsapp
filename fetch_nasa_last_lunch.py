import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from helpers import get_pictures
from datetime import datetime


def fetch_nasa_last_lunch(url: str, demo_key: str, count: int):
    images_path = 'NASA APOD images'
    nasa_payloads = {
        'api_key': f'{demo_key}',
        'count': count
    }
    nasa_response = requests.get(url, params=nasa_payloads)
    nasa_response.raise_for_status()
    nasa_data = json.loads(nasa_response.text)
    nasa_urls = []
    for data in nasa_data:
        nasa_urls.append(data['url'])
    nasa_pics = get_pictures(nasa_urls, images_path=images_path, params=nasa_payloads)


def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA APOD картинок")
    parser.add_argument("-c", "--count", default=None, help="Введите количество картинок: ")
    args = parser.parse_args()
    apod_count = args.count

    load_dotenv()
    demo_key = os.getenv("API_KEY")
    nasa_url = 'https://api.nasa.gov/planetary/apod'
#    nasa_pics = fetch_nasa_last_lunch(nasa_url, demo_key, apod_count)

    if apod_count:
        nasa_pics = fetch_nasa_last_lunch(nasa_url, demo_key, apod_count)
    else:
        nasa_pics = fetch_nasa_last_lunch(nasa_url, demo_key, 30)



if __name__ == '__main__':
    main()
