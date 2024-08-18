import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import get_pictures


def fetch_spacex_id_launch(url: list, api_key: str, id: str):
    payloads = {
        'api_key': f'{api_key}',
        'id': id
    }
    spacex_response = requests.get(url, params=payloads)
    spacex_response.raise_for_status()
    spacex_image_data = spacex_response.json()
    spacex_urls = spacex_image_data['links']['flickr']['original']
    return spacex_urls



def download_spacex_launch(urls: list):
    images_path = 'Space X images'
    spacex_pics = get_pictures(urls, images_path=images_path)
    return spacex_pics





def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания Space X картинок")
    parser.add_argument("-id", "--flight_id", default='5eb87d42ffd86e000604b384', help="Введите ID картинок Space X: ")
    args = parser.parse_args()


    load_dotenv()
    spacex_api_key = os.getenv("NASA_API_KEY")
    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.flight_id}'
    latest_spacex_url = 'https://api.spacexdata.com/v5/launches/latest'
    spacex_id_urls = fetch_spacex_id_launch(spacex_url, spacex_api_key, args.flight_id)
    if args.flight_id:
        spacex_pics = download_spacex_launch(spacex_id_urls)
    else:
        spacex_pics = download_spacex_launch(latest_spacex_url)




if __name__ == '__main__':
    main()
