import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import get_pictures
from itertools import zip_longest


def fetch_epic_lunch(url, api_key, num_images: int):
    images_path = 'NASA EPIC images'
    epic_payloads = {
        'api_key': f'{api_key}',
    }
    epic_response = requests.get(url, params=epic_payloads)
    epic_response.raise_for_status()
    epic_data = json.loads(epic_response.text)
    epic_image_urls = []

    for url in epic_data:
        epic_image_name = [url["image"] for url in epic_data]
        epic_image_period = [url["date"] for url in epic_data]
        for name, period in zip_longest(epic_image_name, epic_image_period, fillvalue='-'):
            epic_image_date = datetime.strptime(period, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
            epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{name}.png?api_key=DEMO_KEY'
            epic_image_urls.append(epic_image_url)
    epic_image = get_pictures(epic_image_urls[0: num_images], images_path=images_path, params=epic_payloads)



def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA EPIC картинок")
    parser.add_argument("-c", "--count", default=10, help="Введите количество картинок: ", type=int)
    args = parser.parse_args()
    epic_count = args.count

    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    epic_info_url = 'https://api.nasa.gov/EPIC/api/natural/'


    epic_pics = fetch_epic_lunch(epic_info_url, nasa_api_key, num_images=epic_count)



if __name__ == '__main__':
    main()