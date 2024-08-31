import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import download_img
from datetime import datetime


def get_nasa_urls(url: str, api_key: str, count: int):
    nasa_payloads = {
        'api_key': f'{api_key}',
        'count': count
    }
    nasa_response = requests.get(url, params=nasa_payloads)
    nasa_response.raise_for_status()
    nasa_image_collection = nasa_response.json()
    nasa_urls = [data for data in nasa_image_collection]
    return nasa_urls





def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA APOD картинок")
    parser.add_argument("-c", "--count", default=30, help="Введите количество картинок: ")
    args = parser.parse_args()
    apod_count = args.count

    load_dotenv()
    nasa_apod_api_key = os.getenv("NASA_API_KEY")
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    images_path = 'NASA APOD images'
    os.makedirs(images_path, exist_ok=True)


    nasa_apod_urls = get_nasa_urls(nasa_url, nasa_apod_api_key, apod_count)


    for image_number, url in enumerate(nasa_apod_urls):
        nasa_apod_pic = download_img(url)
        with open(os.path.join(images_path, f'image_{image_number}{nasa_apod_pic[1]}'), 'wb') as file:
            file.write(nasa_apod_pic[0].content)


if __name__ == '__main__':
    main()
