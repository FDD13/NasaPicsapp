import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import get_pictures
from datetime import datetime


def fetch_nasa_last_lunch(url: str, api_key: str, count: int):
    nasa_payloads = {
        'api_key': f'{api_key}',
        'count': count
    }
    nasa_response = requests.get(url, params=nasa_payloads)
    nasa_response.raise_for_status()
    nasa_image_data = nasa_response.json()
    nasa_urls = [data for data in nasa_image_data]
    return nasa_urls




def download_nasa_pictures(urls: list):
    images_path = 'NASA APOD images'
    nasa_pics = get_pictures(urls, images_path=images_path)
    return nasa_pics





def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания NASA APOD картинок")
    parser.add_argument("-c", "--count", default=30, help="Введите количество картинок: ")
    args = parser.parse_args()
    apod_count = args.count

    load_dotenv()
    nasa_apod_api_key = os.getenv("NASA_API_KEY")
    nasa_url = 'https://api.nasa.gov/planetary/apod'

    nasa_apod_urls = fetch_nasa_last_lunch(nasa_url, nasa_apod_api_key, apod_count)
    nasa_apod_pics = download_nasa_pictures(nasa_apod_urls)



if __name__ == '__main__':
    main()
