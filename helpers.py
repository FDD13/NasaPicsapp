import requests, urllib
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlparse




def get_pictures(urls: list, images_path: str, params: dict):
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    for image_number, url in enumerate(urls):
        response = requests.get(url, params=params)
        response.raise_for_status()
        splitted_url = urllib.parse.urlsplit(url)
        file_name = os.path.basename(url)
        print(splitted_url)
        file_extension = os.path.splitext(splitted_url.path)

        if file_extension[1] == '.png':
            with open(os.path.join(images_path, f'image_{image_number}.png'), 'wb') as file:
                file.write(response.content)
        else:
            with open(os.path.join(images_path, f'image_{image_number}.jpg'), 'wb') as file:
                file.write(response.content)




