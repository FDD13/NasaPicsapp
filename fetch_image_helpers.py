import requests
import urllib
import os
from urllib.parse import urlparse


def download_img(url, images_path, image_number):
    filename = f'image_{image_number}'
    response = requests.get(url)
    response.raise_for_status()
    file_extension = os.path.splitext(url)
    with open(os.path.join(images_path, f"{filename}{file_extension[1]}"), 'wb') as file:
        file.write(response.content)





