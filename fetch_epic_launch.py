import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import download_img
from itertools import zip_longest


def get_epic_urls(url, api_key, num_images: int):
    epic_payloads = {
        'api_key': f'{api_key}'
    }
    epic_response = requests.get(url, params=epic_payloads)
    epic_response.raise_for_status()
    epic_image_collection = epic_response.json()
    epic_image_urls = []


    for url in epic_image_collection:
        epic_image_name, epic_image_period = url.get("image"), url.get("date")
        epic_image_packet = datetime.strptime(url["date"], '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_packet}/png/{epic_image_name}.png'
        epic_image_urls.append(epic_image_url)
    return epic_image_urls






def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA EPIC картинок")
    parser.add_argument("-c", "--count", default=10, help="Введите количество картинок: ", type=int)
    args = parser.parse_args()
    epic_count = args.count

    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    epic_info_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    images_path = 'NASA EPIC images'
    os.makedirs(images_path, exist_ok=True)


    epic_urls = get_epic_urls(epic_info_url, nasa_api_key, num_images=epic_count)



    for image_number, url in enumerate(epic_urls):
        nasa_epic_pic = download_img(url, images_path, image_number)




if __name__ == '__main__':
    main()