import requests
import urllib
import os
from urllib.parse import urlparse




def get_pictures(urls: list, images_path: str, params: dict):
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    for image_number, url in enumerate(urls):
        response = requests.get(url, params=params)
        response.raise_for_status()
        splitted_url = urllib.parse.urlsplit(url)
        file_name = os.path.basename(url)
        file_extension = os.path.splitext(splitted_url.path)
        with open(os.path.join(images_path, f'image_{image_number}.{file_extension}'), 'wb') as file:
            file.write(response.content)




