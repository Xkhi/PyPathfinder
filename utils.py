import requests
from bs4 import BeautifulSoup


def parse_url(core_url, **kwargs):
    raw_url = requests.get(core_url)
    bs4_url = BeautifulSoup(raw_url.text, 'html.parser')

    if len(kwargs) > 0:
        bs4_url = bs4_url.find(kwargs['tag'], kwargs['dict'])

    return bs4_url
