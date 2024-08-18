import requests
import urllib
import os
from urllib.parse import urlparse




def get_pictures(urls: list, images_path: str):
    os.makedirs(images_path, exist_ok=True)
    for image_number, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        splitted_url = urllib.parse.urlsplit(url)
        file_name = os.path.basename(url)
        file_extension = os.path.splitext(splitted_url.path)
        with open(os.path.join(images_path, f'image_{image_number}.{file_extension[1]}'), 'wb') as file:
            file.write(response.content)
            file.close()




