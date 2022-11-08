from mutagen.mp3 import EasyMP3 as MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen.id3._frames import TALB, TCOM

valid_k = EasyID3.valid_keys
# print(valid_k.keys())

def get_tags(mp3_url):
    """Get mp3 tags"""
    music = MP3(mp3_url)
    tags = music.tags
    return tags


def get_info(mp3_url):
    music = MP3(mp3_url)
    info = music.info.length
    return info


url = '/mnt/Files/Projects/mustag_api/mus_tmp/Bo_larkan.mp3'

mus = MP3(url)
print(mus.tags.pprint())
tags = {
    'genre': 'Hi'
}
mus.update(tags)
mus.save()
print('\n')
print(mus.tags.pprint())
# print(get_tags(url))
# print(get_info(url))
