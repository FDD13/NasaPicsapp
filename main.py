import requests
import os
import json
import urllib
import argparse
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urlsplit


def fetch_spacex_last_launch(url, demo_key):
    images_path = 'Space X images'
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    response = requests.get(url)
    data = json.loads(response.text)

    spacex_pics = data['links']['flickr']['original']
    for image_number, image in enumerate(spacex_pics):
        pics_response = requests.get(image)
        pics_response.raise_for_status()
        with open(os.path.join(images_path, f'spacex_{image_number}.jpg'), 'wb') as file:
            file.write(pics_response.content)


def fetch_nasa_last_lunch(url, demo_key):
    images_path = 'NASA APOD images'
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    nasa_payloads = {
        'api_key': f'{demo_key}',
        'count': 30,
    }
    nasa_response = requests.get(url, params=nasa_payloads)
    nasa_response.raise_for_status()
    nasa_data = json.loads(nasa_response.text)

    for image_number, image in enumerate(nasa_data):
        pics_response = requests.get(image['url'], params=nasa_payloads)
        pics_response.raise_for_status()
        with open(os.path.join(images_path, f'nasa_apod_{image_number}.jpg'), 'wb') as file:
            file.write(pics_response.content)
            return pics_response


def file_extension(url, demo_key):
    payloads = {'api_key': f'{demo_key}'}
    picture_data = requests.get(url, params=payloads)
    picture_data.raise_for_status()
    nasa_picture_data = json.loads(picture_data.text)
    nasa_apod_path, nasa_apod_extension = os.path.splitext(nasa_picture_data['url'])
    return nasa_apod_extension


def fetch_epic_lunch(url, demo_key):
    images_path = 'NASA EPIC images'
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    epic_payloads = {
        'api_key': f'{demo_key}',
        'count': 10,
    }
    epic_response = requests.get(url, params=epic_payloads)
    epic_response.raise_for_status()
    epic_data = json.loads(epic_response.text)
    for image_number, image in enumerate(epic_data):
        epic_image_name = epic_data[0]['image']
        epic_image_period = epic_data[0]['date']
        epic_image_date = datetime.strptime(epic_image_period, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{epic_image_name}.png?api_key=DEMO_KEY'
        epic_image = requests.get(epic_image_url, params=epic_payloads)
        with open(os.path.join(images_path, f'nasa_epic_{image_number}.png'), 'wb') as file:
            file.write(epic_image.content)


def main():
    load_dotenv()
    demo_key = os.getenv("API_KEY")
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    epic_info_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
    spacex_pics = fetch_spacex_last_launch(spacex_url, demo_key)
    nasa_pics = fetch_nasa_last_lunch(nasa_url, demo_key)
    epic_pics = fetch_epic_lunch(epic_info_url, demo_key)
    nasa_pics_extension = file_extension(nasa_url, demo_key)
    print(nasa_pics_extension)


if __name__ == '__main__':
    main()
