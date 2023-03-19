[![PyPI version](https://badge.fury.io/py/radiojavanapi.svg)](https://badge.fury.io/py/radiojavanapi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/xHossein/radiojavanapi/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/radiojavanapi)](https://pepy.tech/project/radiojavanapi)

# radiojavanapi
**radiojavanapi** is a Python library for accessing RadioJavan's features. With this library you can create Telegram Bots with ease and simplicity.

Support Python >= 3.7

RadioJavan API valid for 19 March 2023 (last reverse-engineering check)

## Features
* Get full info of a Song, Video, Podcast, Story, Playlist, Artist, Album, User and your Account
* Login by email and password
* Sign up to RadioJavan
* Like and Unlike a Song, Video, Podcast and Story
* Follow and Unfollow a Artist, User or MusicPlaylist
* Get followers and following of a user
* Create, Rename and Delete a playlist
* Add song or video to playlist or Remove from it
* Edit and Deactive account
* Upload and Remove profile photo
* Search and get trending, popular and ... medias\
and much more else

## Installation
**From PyPI**
```
pip install radiojavanapi
```

**From Github**
```
pip install git+https://github.com/xHossein/radiojavanapi@master
```

## Basic Usage

```python
from radiojavanapi import Client

# Create a Client instance and get a song info. 
client = Client()
song = client.get_song_by_url(
            'https://www.radiojavan.com/mp3s/mp3/Sijal-Baz-Mirim-Baham-(Ft-Sami-Low)')

print(f"""
        Name: {song.name}
        Artist: {song.artist}
        HQ-Link: {song.hq_link}
""")

```
<details>
    <summary>Show Output</summary>

```
Name: Baz Mirim Baham (Ft Sami Low)
Artist: Sijal
HQ-Link: https://host2.mediacon-rj.app/media/mp3/aac-256/99926-cf9dd3814907dbb.m4a
```
</details>

## Documentation
You can find the documentation [here](https://xhossein.github.io/radiojavanapi/).

## Support

- Create a [GitHub issue](https://github.com/xHossein/radiojavanapi/issues) for bug reports, feature requests, or questions
- Add a ⭐️ [star on GitHub](https://github.com/xHossein/radiojavanapi) to support the project!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog
You can find this repository's changelog [here](https://github.com/xHossein/radiojavanapi/blob/master/CHANGELOG.md).

## License
This project is licensed under the [MIT license](https://choosealicense.com/licenses/mit/).
