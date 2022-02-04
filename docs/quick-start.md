# Quick Start

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

# Create a Client instance. and set a proxy (Optional)
client = Client()
client.set_proxy({
            'http':'socks5://127.0.0.1:8087'
            'https':'socks5://127.0.0.1:8087'
            })

song = client.get_song_by_url(
            'https://www.radiojavan.com/mp3s/mp3/Sijal-Baz-Mirim-Baham-(Ft-Sami-Low)')

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

!> Please note that `set_proxy` only gets proxy as dict.
