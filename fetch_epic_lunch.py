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


def fetch_epic_lunch(url, demo_key, num_images: int):
    images_path = 'NASA EPIC images'
    epic_payloads = {
        'api_key': f'{demo_key}',
    }
    epic_response = requests.get(url, params=epic_payloads)
    epic_response.raise_for_status()
    epic_data = json.loads(epic_response.text)
    epic_image_urls = []
    for url in epic_data:
        epic_image_name = epic_data[0]['image']
        epic_image_period = epic_data[0]['date']
        epic_image_date = datetime.strptime(epic_image_period, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{epic_image_name}.png?api_key=DEMO_KEY'
        epic_image_urls.append(epic_image_url)
    print(epic_image_urls)
    epic_image = get_pictures(epic_image_urls[0:num_images], images_path=images_path, params=epic_payloads)
    return epic_image



def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA EPIC картинок")
    parser.add_argument("-c", "--count", default=None, help="Введите количество картинок: ", type=int)
    args = parser.parse_args()
    epic_count = args.count

    load_dotenv()
    demo_key = os.getenv("API_KEY")
    epic_info_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'

    if epic_count:
        epic_pics = fetch_epic_lunch(epic_info_url, demo_key, epic_count)
    else:
        epic_pics = fetch_epic_lunch(epic_info_url, demo_key, 10)


if __name__ == '__main__':
    main()