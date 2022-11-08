import requests
from pprint import pprint


URL = 'http://127.0.0.1:8000/api/'

def upload_mus():
    URL_ = URL + 'upload/'

    file = open(file='/mnt/Files/Music/Bo_larkan.mp3', mode='rb')

    files = {'music_file': file}
    json = {'parameters': {'time_second':200}}
    resp = requests.post(url=URL_, files=files, json=json)

    return resp.json()


def get_valid_keys():
    URL_ = URL + 'get_valid_tags/'

    resp = requests.get(url=URL_)

    return resp.json()


def get_t():
    URL_ = URL + 'get_tags/'

    json = {
        'm_id': '',
    }



def update_t():
    URL_ = URL + 'update_music/'

    json = {
        'music_id': '2c1da53a-17d5-4238-8e5e-fa68d85a3bbb',
        'update': {'genre':'Birnima2'},
    }
    resp = requests.post(url=URL_, json=json)

    return resp.json()


pprint(get_valid_keys())
