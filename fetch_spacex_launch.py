import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, urlsplit
from fetch_image_helpers import download_img


def get_spacex_urls(url, id: str):
    spacex_response = requests.get(url)
    spacex_response.raise_for_status()
    spacex_image_packet = spacex_response.json()
    spacex_urls = spacex_image_packet['links']['flickr']['original']
    return spacex_urls





def main():
    parser = argparse.ArgumentParser(description="Программа для скачивания Space X картинок")
    parser.add_argument("-id", "--flight_id", default='5eb87d42ffd86e000604b384', help="Введите ID картинок Space X: ")
    args = parser.parse_args()


    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.flight_id}'
    latest_spacex_url = 'https://api.spacexdata.com/v5/launches/latest'
    images_path = 'Space X images'
    os.makedirs(images_path, exist_ok=True)

    spacex_pics_urls = get_spacex_urls(spacex_url, args.flight_id)


    for image_number, url in enumerate(spacex_pics_urls):
        spacex_pic = download_img(url, images_path, image_number)







if __name__ == '__main__':
    main()
