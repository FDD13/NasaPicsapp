import requests
import urllib
import os
from urllib.parse import urlparse


def download_img(url):
    response = requests.get(url)
    response.raise_for_status()
    file_extension = os.path.splitext(url)
    return response, file_extension[1]




