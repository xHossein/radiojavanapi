# Quick Start

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

# Create a Client instance. Setting a proxy is optional.
client = Client()
client.set_proxy({
            'http': 'socks5://127.0.0.1:8087',
            'https': 'socks5://127.0.0.1:8087'
            })

song = client.get_song_by_url(
            'https://play.radiojavan.com/song/sijal-baz-mirim-baham-(ft-sami-low)')

print(f"""
        Name: {song.name}
        Artist: {song.artist}
        Plays: {song.plays}
        Downloads: {song.downloads}
        HQ-Link: {song.hq_link}
""")

```
<details>
    <summary>Show Output</summary>

```
Name: Baz Mirim Baham (Ft Sami Low)
Artist: Sijal
Plays: 693934
Downloads: 693934
HQ-Link: https://host2.mediacon-rj.app/media/mp3/aac-256/99926-cf9dd3814907dbb.m4a
```
</details>

!> `set_proxy()` only accepts a `dict` as its argument. If you do not need a proxy, skip this call entirely.
