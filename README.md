![PyPI - Version](https://img.shields.io/pypi/v/radiojavanapi)
![GitHub License](https://img.shields.io/github/license/xhossein/radiojavanapi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/radiojavanapi)

# radiojavanapi
**radiojavanapi** is a Python library and wrapper for the RadioJavan API. It lets you build bots, streaming applications, download tools, and automation scripts with minimal effort.

Requires Python >= 3.7

The RadioJavan API was last reverse-engineered and verified on 3 August 2026.

## Features
* Get full info for a Song, Video, Podcast, Story, Playlist, Artist, Album, or User, as well as your own Account
* Log in with an email and password
* Sign up to RadioJavan
* Like and unlike a Song, Video, Podcast, or Story
* Follow and unfollow an Artist, User, or MusicPlaylist
* Get a user's followers and following
* Create, rename, and delete playlists
* Add a song or video to a playlist, or remove it
* Edit and deactivate your account
* Upload and remove your profile photo
* Search, and get trending, popular, and featured media
* And much more

## Installation
**From PyPI**
```
pip install radiojavanapi
```

**From GitHub**
```
pip install git+https://github.com/xHossein/radiojavanapi@master
```

## Basic Usage

```python
from radiojavanapi import Client

# Create a Client instance and get song info. 
client = Client()
song = client.get_song_by_url(
            'https://play.radiojavan.com/song/sijal-baz-mirim-baham-(ft-sami-low)')

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
The documentation is available [here](https://xhossein.github.io/radiojavanapi/).

## Support

- Open a [GitHub issue](https://github.com/xHossein/radiojavanapi/issues) for bug reports, feature requests, or questions
- Add a ⭐️ [star on GitHub](https://github.com/xHossein/radiojavanapi) to support the project!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog
You can find this repository's changelog [here](https://github.com/xHossein/radiojavanapi/blob/master/CHANGELOG.md).

## License
This project is licensed under the [MIT license](https://choosealicense.com/licenses/mit/).
