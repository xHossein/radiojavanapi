# radiojavanapi
**radiojavanapi** is a Python library for accessing RadioJavan's features. With this library you can create Telegram Bots with ease and simplicity.

Support Python >= 3.6

RadioJavan API valid for 8 February 2021 (last reverse-engineering check)

# Features
* Get full info of a Song/Video/Podcast/Story/Playlist/Artist/Album/Account
* Like/Unlike Song/Video/Podcast/Story
* Follow/Unfollow a Artist/MusicPlaylist
* Create/Rename/Delete a playlist and Add song/video to it or Remove from it
* Edit/Deactive account
* Upload/Remove profile photo
* Search and get trending/popular/... medias\
and much more else

## Install
```
pip install radiojavanapi
```
<br>

# Usage
**Create the client**

```bash
from radiojavanapi import Client
from radiojavanapi.exceptions import *

# Create a Client object. and set a proxy (Optional)
client = Client()
client.set_proxy({'http':'socks5://127.0.0.1:8087'})
```
> Please note that `set_proxy` only gets proxy as dict.

**Log in to radiojavan (Optional)**\
for some methods you must been authorized.
```bash
from radiojavanapi.exceptions import *

try:
    client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
except BadCredentials:
    # raise due to wrong email or password
    # do something
```
## Types
The current types are in [types.py](https://github.com/xHossein/radiojavanapi/blob/master/radiojavanapi/types.py):

Model | Description
-------|------------
Account | Full private info for your account (e.g. email, stories)
Song | Full public Song(mp3) data
Video | Full public Video data
Podcast | Full public Podcast data
Artist | Full public Artist data
MusicPlaylist | Full public Music Playlist data
VideoPlaylist | Full public Video Playlist data
Album | Full public Album data
Story | Full public Story(selfies) data
Profile | Full public data of user who uploaded story  
ComingSoon | Full public data of coming soon song/video
SearchResults | Result of search

## **Account**
This is your authorized account
Method | Return | Description | Login Require
-------|--------|------------|------------
Client() | bool | Init radiojavanapi client | NO
login(email: str, password: str) | bool | Login by email and password | NO
set_proxy(proxy: dict) | None | Support socks and http/https proxy | NO
unset_proxy() | None | Remove proxy  | NO
account_info() | Account | Get private info for your account (e.g. email, stories) | YES
account_edit(data: dict) | Account | Change profile data (e.g. email, firstname, lastname, username) | YES
change_photo(photo_path: str) | bool | Set photo as your profile photo (support jpg/png) | YES
remove_photo() | Account | Remove your current profile photo | YES
change_password(password: str) | bool | Change account password | YES
deactive_account() | bool | Deactive the account and logout | YES
my_following() | List[str] | Get list of artists name which you follow | YES
my_playlists() | Dict | Return video & music playlist's id and title as dict | YES

Example:
```bash
>>> client.account_info().dict()
{'name': 'Hossein xxxxxxx',
'firstname': 'Hossein',
'lastname': 'xxxxxxx',
'display_name': '@Hossein',
'username': 'xhosseinxxx',
'share_link': HttpUrl('https://rj.app/u/xhosseinxxx',...'),
'email': 'testacc@test.com',
'has_subscription': False,
'custom_photo': False,
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/profiles/default-profile.jpg',...'),
'thumbnail': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/profiles/default-profile-thumb.jpg', ...'),
'playlists_count': 5,
'songs_count': 132,
'artists_count': 1,
'artists_name': ['Ashvan'],
'stories': []
}


>>> client.account_edit({'username':'your new username'})
# return Account object

>>> client.account_edit({'firstname':'fname','lastname':'lname','email':'new email'})
# return Account object

>>> client.change_photo('./folder/image.jpg')
True

>>> client.my_playlists()
{
'music_playlists': [
    {'id': 'f72225afg2da', 'title': 'test1'},
    {'id': '7222629c22f9', 'title': 'test2'}
    ],
'video_playlists': [
    {'id': '26276c622618', 'title': 'test1'},
    {'id': 'e6261s6c22c8', 'title': 'test2'},
    {'id': '9226c6c79sa3', 'title': 'test3'}
    ]
}
```
<br><br>
## **Song** ( RJ api calls it `mp3` )

Method | Return | Description | Login Require
-------|--------|------------|------------
get_song_by_url(url: str) | Song | Return song info by site url (radiojavan.com) | NO
get_song_by_id(id: int) | Song | Return song info by id | NO
like_song(song: Song) | bool | Like a song | YES
unlike_song(song: Song) | bool | UnLike a song | YES
liked_songs() | List[Song] | Get list of songs you liked | YES

<br>Example:
```bash
>>> client.get_song_by_url('https://www.radiojavan.com/mp3s/mp3/Nikita-SheryM-Boom-Boom').dict()
{
'id': 94010,
'title': 'Nikita & SheryM - "Boom Boom"',
'artist': 'Nikita & SheryM',
'song': 'Boom Boom',
'likes': 6268,
'dislikes': 64,
'plays': 3837527,
'downloads': 3837527,
'type': 'mp3',
'item': None,
'album': None,
'date': 'Aug 7, 2020',
'created_at': '2020-08-07T18:38:55-04:00',
'duration': 201.665,
'permlink': 'Nikita-SheryM-Boom-Boom',
'link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/mp3-256/94010-e68b5de09360ffe.mp3',...),
'hq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/aac-256/94010-e68b5de09360ffe.m4a',...),
'lq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/aac-128/94010-e68b5de09360ffe.m4a',...), 
'hls_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/mp3-hls/94010-e68b5de09360ffe/playlist.m3u8',...),
'hq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/mp3-hls/94010-e68b5de09360ffe/playlist.m3u8', ...),
'lq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/mp3/mp3-hls/94010-e68b5de09360ffe/file-96k.m3u8',...),
'comments_link': HttpUrl('https://www.radiojavan.com/services/comments?type=mp3&id=94010',...'),
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/mp3/nikita-sherym-boom-boom/1dbc026b08d8b4c.jpg',...),
'photo_player': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/mp3/nikita-sherym-boom-boom/d6374f71fc0bd15-player.jpg',...),
'share_link': HttpUrl('https://rj.app/m/dv2P1Xwq',...),
'thumbnail': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/mp3/nikita-sherym-boom-boom/1dbc026b08d8b4c-thumb.jpg',...),
'credit_tags': ['nikita', 'sherym'],
'credits': None,
'artist_tags': ['Nikita', 'SheryM'],
'lyric': 'موزیکامون بوم بوم بوم \nچشا رومه زوم زوم زوم\nبیا نزدیکتر پیشم انگار گوله آتیشم \nهمه پیکا بالاس بیا آ\n\nمیخوای که مال تو باشم \nرو کن چی داری تو واسم \nبعد یه سره حواسم از دست تو\n\nمستیم پع نوش غم فراموش \nهستیم تا خود صبح فردا رو پامون\n\nموزیکامون بوم بوم بوم \nچشا رومه زوم زوم زوم\nخود بازیا ازم راضین \nتوی هم جمعا من آس بازیم\n\nمیگم پا نمیده بد ازش شاکین\nکل شهر دنبالمه تو هم سر خط منتظر تو ایستگاه\nپا رو گاز یکیم میگه واینستا قفلی بزارش رو تکرار\n\nموزیکامون 
بوم بوم بوم \nچشا رومه زوم زوم زوم\nکل شهر دنبالم میگه هواتو دارم\nاگه بشی صاحب قلبم میدم دنیارو واست\n\nبدی عشقو نشونم یکی یدونم \nفقط یادت باشه نشکنی دلو آروم جونم\nموزیکامون بوم بوم بوم چشا رومه زوم زوم زوم\n\nمیای جلو میگی خوبم خودم میدونم \nدعوا سر منه هر جا برم دیوونم\nمیشن میفتن همه دنبال ردم\n\nمنم واسه خودم یه گوشه ای سرگرم \nاینجا همه کولیم فاز بالا گنگ گنگ\nپیکو برو بالا سلامتی جمع اینجا \nجای عاشقی نیس پسر خوب اصلا',
'related_songs_id': [
93312, 91891, 91020, 96448, 96288, 82969, 87697, 85457, 85089, 94136, 82967, 88146, 83723, 77401, 94639, 88976, 80945, 92558, 58758, 81550, 68648, 93717, 86527, 82970, 94774, 72749, 93479, 88416, 86866, 78988
],
'stories': [ .. list of stories object .. ]
}

>>> songObj = client.get_song_by_url('https://www.radiojavan.com/mp3s/mp3/Nikita-SheryM-Boom-Boom')
... client.like_song(songObj)
True

>>> client.liked_songs()
[ list of song object ]

```
<br><br>
## **Video**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_video_by_url(url: str) | Video | Return video info by site url (radiojavan.com) | NO
get_video_by_id(id: int) | Video | Return video info by id | NO
like_video(video: Video) | bool | Like a video | YES
unlike_video(video: Video) | bool | UnLike a video | YES
liked_videos() | List[Video] | Get list of videos you liked | YES

<br>Example:
```bash
>>> client.get_video_by_url('https://www.radiojavan.com/mp3s/mp3/Nikita-SheryM-Boom-Boom').dict()
{
'id': 7302,
'title': 'Nikita & SheryM - "Boom Boom"',
'artist': 'Nikita & SheryM',
'song': 'Boom Boom',
'likes': 1379,
'dislikes': 38,
'views': 708370,
'type': 'video',
'item': None,
'date': 'Sep 7, 2020',
'created_at': '2020-09-07T20:34:05-04:00',
'artist_tags': ['Nikita', 'SheryM'],
'credit_tags': ['nikita', 'sherym'],
'permlink': 'nikita-sherym-boom-boom',
'link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/music_video/hq/nikita-sherym-boom-boom.mp4',...),
'hq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/music_video/hd/nikita-sherym-boom-boom.mp4',...),
'lq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/music_video/hq/nikita-sherym-boom-boom.mp4',...),
'hq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/music_video/hls/nikita-sherym-boom-boom/playlist.m3u8',...),
'lq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/music_video/hls/nikita-sherym-boom-boom/playlist.m3u8',...),
'comments_link': HttpUrl('https://www.radiojavan.com/services/comments?type=video&id=7302',...),
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/musicvideos/images/f89b8151c74f74f-original-larger.jpeg',...),
'photo_player': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/musicvideos/images/nikita-sherym-boom-boom/d8c59c40700b4d2-player.jpg',...),
'share_link': HttpUrl('https://rj.app/v/BN0WmaPk',...),
'related_video_id': [
5542, 7160, 6751, 6848, 6496, 5886, 5635, 4693, 5483, 6519, 7601, 6458, 4152, 5307, 6507, 5644, 4797, 6026, 4009, 5742, 7447, 5413, 5740, 6366, 5201, 6003, 3521, 3932, 2086, 6894
    ]
}

>>> videoObj = client.get_video_by_url('https://www.radiojavan.com/videos/video/nikita-sherym-boom-boom')
... client.like_video(videoObj)
True

>>> client.liked_videos()
[ list of video object ]

```
<br><br>
## **Podcast**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_podcast_by_url(url: str) | Podcast | Return podcast info by site url (radiojavan.com) | NO
get_podcast_by_id(id: int) | Podcast | Return podcast info by id | NO
like_podcast(podcast: Podcast) | bool | Like a podcast | YES
unlike_podcast(podcast: Podcast) | bool | UnLike a podcast | YES

<br>Example:
```bash
>>> client.get_podcast_by_url('https://www.radiojavan.com/podcasts/podcast/Abo-Atash-118').dict()
{
'id': 3111,
'title': 'Abo Atash',
'likes': 5325,
'dislikes': 27,
'plays': 1553141,
'type': 'podcast',
'talk': False,
'date': 'Episode 118',
'short_date': 'Episode 118',
'created_at': '2021-01-26T00:00:00-05:00',
'duration': 2686.69,
'permlink': 'Abo-Atash-118',
'show_permlink': 'Abo-Atash',
'credit_tags': ['dj taba'],
'link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/mp3-192/3111-44693e07c51c098.mp3',...),
'hq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/aac-192/3111-44693e07c51c098.m4a',...),
'lq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/aac-128/3111-44693e07c51c098.m4a',...),
'hls_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/podcast-hls/3111-44693e07c51c098/playlist.m3u8',...),
'hq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/podcast-hls/3111-44693e07c51c098/playlist.m3u8',...),
'lq_hls': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/podcast/podcast-hls/3111-44693e07c51c098/file-96k.m3u8',...),
'comments_link': HttpUrl('https://www.radiojavan.com/services/comments?type=podcast&id=3111',...),
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/podcasts/abo-atash-118/5618b07d818299c.jpg',...),
'photo_player': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/podcasts/abo-atash-118/5cef5f1f0d1b737-player.jpg',...),
'share_link': HttpUrl('https://rj.app/p/RyY7QOxv',...),
'thumbnail': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/podcasts/abo-atash-118/5618b07d818299c-thumb.jpg',...),
'tracklist': 'Arta - Erade Kon (Ft Koorosh & Khashayar SR) Remix\r\nBuray - Karma (Aytac 
Kart Remix) Aytac Kart Remix \r\nAnita - Vaghti Hava Migire\r\nPuzzle - Memorable Medley 2\r\nShadmehr Aghili - Baroon Delam Khast \r\nSogand - Tehran\r\nAmir Tataloo - Rooz Be Rooz (Remix)\r\nNaser Zeynali - Delbare Nab\r\nOffaiah - Play It By Ear (Club Mix) \r\nKiyarash - Baghal\r\nHayedeh - Golvajeh (Dynatonic Remix)\r\nEbi - Goriz \r\nGoogoosh - Talagh (Extended Club Mix)\r\nFranky Rizardo - Olympus\r\nClaptone - Under The Moon (Ft Nathan Nicholson)\r\nAlireza JJ, Sijal, & Nassim - Hese Lamese (Ft Sami Low) \r\nDavi - Lie Machine (Gorgon City Remix) \r\nJim Rider - In Theory (Original Mix)\r\nHomayoun Shajarian - Ahay Khabardar (Remix)\r\nDJ Dark & MD DJ - Il padrino (Extended Mix)\r\nNamito - Stone Flower',
'related_podcast_id': [
3073, 2893, 2836, 2767, 2729, 2650, 2594, 2447, 2308, 2248, 2194, 2146, 2116, 2069, 1962, 1820, 1774, 1751, 1653, 1590, 1552, 1416, 1383, 1352, 1314, 1244, 1237, 1203, 1183, 1116
    ]
}

>>> podcastObj = client.get_podcast_by_url('https://www.radiojavan.com/podcasts/podcast/Abo-Atash-118')
... client.like_podcast(podcastObj)
True

``` 
<br><br>
## **Album**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_album_by_url(url: str) | Optional[Album] | Return album info by site url (radiojavan.com) | NO
get_album_by_id(id: int) | Optional[Album] | Return album info by id (this id belong to one of tracks) | NO

<br>Example:
```bash
>>> client.get_album_by_url('https://www.radiojavan.com/mp3s/album/Sogand-Man').dict()
{
'id': '96327',
'created_at': '2020-12-24T07:33:55-05:00',
'date': 'Dec 24, 2020',
'tracks': [ list of songs object],
'album': 'Man',
'artist': 'Sogand',
'share_link': HttpUrl('https://rj.app/ma/e7YWjW18',...)
}

```
<br><br>
## **Artist**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_artist_by_url(url: str) | Artist | Return artist info by site url (radiojavan.com) | NO
get_artist_by_name(name: int) | Artist | Return artist info by name (must be correct name) | NO
follow_artist(artist: Artist) | bool | Follow a artist | YES
unfollow_artist(artist: Artist) | bool | UnFollow a artist | YES

<br>Example:
```bash
>>> client.get_artist_by_url('https://www.radiojavan.com/artist/Satin').dict()
{
'name': 'Satin',
'latest_song_id': 96242,
'followers_count': 30270,
'following': False,
'plays': '294M',
'background': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/artists/photos/satin-f2a8958ded0b763-photo.jpg',...),
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/artists/photos/satin-f2a8958ded0b763-photo.jpg',...),
'photo_player': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/artists/photos/satin-88b142dfb09c009-player.jpg',...),
'photo_thumb': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/artists/photos/satin-f2a8958ded0b763-photo-thumb.jpg',...),
'share_link': HttpUrl('https://rj.app/a/WMvMR2yZ',...),
'prereleases': [],
'events': [],
'photos': [],
'songs_id': [
96118, 94639, 88146, 91078, 93479, 87259, 94638, 86293, 89582, 94640, 96242, 83102, 90267, 82753, 82913, 85772, 92694, 84907, 86529, 88858, 83077, 85431, 83635, 77005, 73645, 82203, 80536, 76254, 72394, 69936, 59001
],
'albums_id': [
    94638
],
'videos_id': [
7601, 6458, 5644, 5635, 6026, 5665, 6803, 7210, 5912
], 
'podcasts_id': [],
'playlists_id': [
    '37635f81c823'
    ]
}

>>> artistObj = client.get_artist_by_url('https://www.radiojavan.com/artist/Satin')
... client.follow_artist(artistObj)
True

```
<br><br>
## **Story** ( RJ api calls it `selfie` )

Method | Return | Description | Login Require
-------|--------|------------|------------
get_story_by_url(url: str) | Story | Return story info by site url (radiojavan.com) | NO
get_story_by_hash_id(hash_id: str) | Story | Return story info by hash_id | NO
like_story(story: Story) | bool | Like a story | YES
unlike_story(story: Story) | bool | UnLike a story | YES

<br>Example:
```bash
>>> client.get_story_by_url('https://www.radiojavan.com/story/mxE3Ybyg').dict()
{
'id': 289965,
'hash_id': 'mxE3Ybyg',
'title': 'Shadmehr Aghili - "Avaz Nemishi"',
'song': 'Avaz Nemishi',
'song_id': 96835,
'artist': 'Shadmehr Aghili',
'verified': False,
'type': 'selfie',
'likes': '681', 
'likes_pretty': '681',
'filename': '289965-ee9c65128c566f5',
'link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/selfie/7677570/289965-ee9c65128c566f5.mp4',...),
'lq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/selfie/7677570/hd/289965-ee9c65128c566f5.mp4',...),
'hq_link': HttpUrl('https://d1ek016ppw7pfv.cloudfront.net/media/selfie/7677570/289965-ee9c65128c566f5.mp4',...),
'share_link': HttpUrl('https://rj.app/story/mxE3Ybyg',...),
'photo': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/selfie/7677570/66eb9642897545d.jpg',...),
'thumbnail': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/selfie/7677570/66eb9642897545d-thumb.jpg',...),
'user': { #this is profileObject.dict()
    'thumbnail': HttpUrl('https://d2hudtqn98uvom.cloudfront.net/static/profiles/7677570/fd7f44f9ddbfe5b-thumb.jpg',...),
    'username': 'hengamehtorknezhad',
    'display_name': '@hengamehtorknezhad'
    },
'location': 'Germany',
'is_mystory': False
}

>>> storyObj = client.get_story_by_url('https://www.radiojavan.com/story/mxE3Ybyg')
... client.like_story(storyObj)
True

```
<br><br>

## **MusicPlaylist**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_music_playlist_by_url(url: str) | MusicPlaylist | Return music playlist info by site url (radiojavan.com) | NO
get_music_playlist_by_id(id: str) | MusicPlaylist | Return music playlist info by id | NO
follow_music_playlist(music_playlist: MusicPlaylist) | bool | Follow a music playlist | YES
unfollow_music_playlist(music_playlist: MusicPlaylist) | bool | UnFollow a music playlist | YES
create_music_playlist(name: str, song: Song) | Optional[str] | Create a music playlist and return its id | YES
rename_music_playlist(music_playlist: MusicPlaylist, new_name: str) | bool | Rename your music playlist | YES
delete_music_playlist(music_playlist: MusicPlaylist) | bool | Delete your music playlist | YES
add_to_music_playlist(music_playlist: MusicPlaylist, song: Song) | bool | Add a song to your music playlist | YES
remove_from_music_playlist(music_playlist: MusicPlaylist, song: Song) | bool | Remove a song from your music playlist | YES

## **VideoPlaylist**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_video_playlist_by_url(url: str) | VideoPlaylist | Return video playlist info by site url (radiojavan.com) | NO
get_video_playlist_by_id(id: str) | VideoPlaylist | Return video playlist info by id | NO
create_video_playlist(name: str, video: Video) | Optional[str] | Create a video playlist and return its id | YES
rename_video_playlist(video_playlist: VideoPlaylist, new_name: str) | bool | Rename your video playlist | YES
delete_video_playlist(video_playlist: VideoPlaylist) | bool | Delete your video playlist | YES
add_to_video_playlist(video_playlist: VideoPlaylist, video: Video) | bool | Add a video to your video playlist | YES
remove_from_video_playlist(video_playlist: VideoPlaylist, video: Video) | bool | Remove a video from your video playlist | YES


## **Search**

Method | Return | Description | Login Require
-------|--------|------------|------------
search(query: str) | SearchResults | Return search results object | NO
get_trending_searches() | List[str] | Return string list of trending searches | NO

<br>Example:
```bash
>>> client.search('nikita boom boom').dict()
{
'query': 'nikita boom boom',
'songs_id': [
    94010, 96448, 76841, 80945, 88976, 82964, 83723, 87697, 81999, 84468, 85457, 72749, 82966, 82967, 86866, 82965, 82970, 78988, 82968, 82969
    ],
'albums_id': [82964],
'videos_id': [7302, 5542, 6751, 6496, 5270, 5413],
'podcasts_id': [],
'playlists_id': [],
'artists_name': [],
'lyrics': [],
'shows': [],
'profiles': []
}

>>> client.get_trending_searches()
['tm bax', 'mohsen ebrahimzadeh', 'mohsen chavoshi', 'moein', 'sohrab mj']

```
<br><br>

## **Browse**

Method | Return | Description | Login Require
-------|--------|------------|------------
get_latest_stories() | List[Story] | Return list of latest stories | NO
get_trending_songs() | List[Song] | Return list of trending songs | NO
get_popular_songs() | List[Song] | Return list of popular songs | NO
get_featured_songs() | List[Song] | Return list of featured songs | NO
get_latest_albums() | List[Album] | Return list of latest albums | NO
get_trending_videos() | List[Video] | Return list of trending videos | NO
get_popular_videos() | List[Video] | Return list of popular videos | NO
get_featured_videos() | List[Video] | Return list of featured videos | NO
get_latest_videos() | List[Video] | Return list of latest videos | NO
get_popular_podcasts() | List[Podcast] | Return list of popular podcasts | NO
get_featured_podcasts() |List[Podcast] | Return list of featured podcasts | NO
get_talk_podcasts() | List[Podcast] | Return list of talk podcasts | NO
get_shows_podcasts() | List[Podcast] | Return list of shows podcasts | NO
get_popular_artists() | List[Artist] | Return list of popular artists | NO
get_coming_soon() | List[ComingSoon] | Return list of comingsoon songs/videos | NO
<br>

## **Common Exceptions**
Exception | Base | Description
----------|------|------------
ClientError | Exception | Base Exception for RadioJavan calls
ClientJSONDecodeError | ClientError | JSON Exception
ClientLoginRequired | ClientError | Raised when RadioJavan required Login
<br>

## **Private Exceptions**
Exception | Base | Description
----------|------|------------
PrivateError | ClientError | Base Exception for Private calls
BadCredentials | PrivateError | Raise when email/password is wrong
OnlyContainLetters | PrivateError | Raise when firstname/lastname contains digits (edit account)
LongString | PrivateError | Raise when string is too long (edit account)
EmailExists | PrivateError | Raise when email used by another account (edit account)
UsernameExists | PrivateError | Raise when username used by another account (edit account)
NameExists | PrivateError | Raise when use duplicate name (rename playlist)
PlayListExists | PrivateError | Raise when use duplicate name (create playlist)
UnknownError | PrivateError | Raise when get unknown message (new message from radiojavan)

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html). Hence, when pushing commits, it is encouraged to use the described formatting and use the following keywords:

* `Added` for new features.
* `Changed` for changes in existing functionality.
* `Deprecated` for soon-to-be removed features.
* `Removed` for now removed features.
* `Fixed` for any bug fixes.
<br><br>
# Changelog
You can find this repository's changelog here: [CHANGELOG](https://github.com/xHossein/radiojavanapi/blob/master/CHANGELOG.md) 
<br><br>
# License
[MIT](https://choosealicense.com/licenses/mit/)
