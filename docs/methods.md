# Methods

## Authentication
For [Actions](methods?id=actions) and [Account](methods?id=account) methods, you must have an account.

### Login
Arguments:

| Name | Type | Description
-------|------|------------
`email` | `str` | Your account email
`password` | `str` | Your account password

Example:
```python
from radiojavanapi import Client
from radiojavanapi.exceptions import BadCredentials

client = Client()
try:
    client.login("YOUR EMAIL", "YOUR PASSWORD")
except BadCredentials:
    # raise due to wrong email or password
    # do something
    pass

song = client.get_song_by_url(
            'https://www.radiojavan.com/mp3s/mp3/Sijal-Baz-Mirim-Baham-(Ft-Sami-Low)')

print(client.like_song(song.id))
print(client.follow_artist(song.artist))
```
<details>
    <summary>Show Output</summary>

```
True
True
```
</details>

### Sign Up

Arguments:

| Name | Type | Description
-------|------|------------
`firstname` | `str` | Your account firstname
`lastname` | `str` | Your account lastname
`username` | `str` | Your account username
`email` | `str` | Your account email
`password` | `str` | Your account password
`auto_login` | `bool` | Login to account after sign up

Example:
```python
from radiojavanapi import Client

client = Client()
client.signup("YOUR FIRSTNAME", "YOUR LASTNAME", "YOUR USERNAME", "YOUR EMAIL", "YOUR PASSWORD", True)
```

### Save & Load session
You can save your session like this:
```python
clientObj.save_session('./myaccount')
```
And you can load your session as well to avoid many logins:
```python
clientObj.load_session('./myaccount')
```

## Account
All account methods require authentication.

?> **Radiojavanapi Docs:** Check [here](methods?id=authentication) for login or sign up.

### Activity
- Get list of:
    - Your followers & following
    - Song & video you've liked befor
    - Artist you're following now.

Method | Return | Description | Login Required
-------|------------|-------------|--------------
liked_songs() | `list[`[Song](models?id=song)`]` | Returns list of songs you've liked | YES
liked_videos() | `list[`[Video](models?id=video)`]` | Returns list of videos you've liked | YES
following_artists() | `list[str]` | Returns list of artist names which you've followed | YES
my_followers() | `list[`[ShortUser](models?id=shortuser)`]` | Returns list of your followers | YES
my_following() | `list[`[ShortUser](models?id=shortuser)`]` | Returns list of your following| YES
my_playlists() | [MyPlaylists](models?id=myplaylists) | Returns your video & music playlist's | YES

### Update
Update your account.

Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
account_edit() | <ul><li>`(Optional) firstname: str`</li><br/><li>`(Optional) lastname: str`</li><br/><li>`(Optional) username: str`</li><br/><li>`(Optional) email: str`</li><br/><li>`(Optional) bio: str`</li></ul> | [Account](models?id=account) | Change profile data | YES
account_notifications_update() | <ul><li>`(Optional) new_music: bool`</li><br/><li>`(Optional) followed_artists: bool`</li><br/></ul> | `bool` | Update your notifications settings | YES
change_password() | `password: str`<br/>`(Your new passowrd)` | `bool` | Change your account password | YES
upload_photo() | `photo_path: str` | `bool` | Upload your profile photo (only jpg/png) | YES
remove_photo() |   | `bool` | Remove your profile photo | YES

!> To remove bio, pass an empty string.

### Others
Method | Return | Description | Login Required
-------|--------|-------------|--------------
account_info() | [Account](models?id=account) | Returns private info of your account | YES
account_notifications() | [NotificationsStatus](models?id=notificationsstatus) | Returns status of current notifications settings | YES
deactive_account() | `bool` | Deactivate your account and logout | YES


## Actions
All action methods require authentication.

?> **Radiojavanapi Docs:** Check [here](methods?id=authentication) for login or sign up.

### Like & Unlike

Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
like_song() | `song_id: Union[int, str]` | `bool` | Like a song | YES
unlike_song() | `song_id: Union[int, str]` | `bool` | Unlike a song | YES
like_video() | `video_id: Union[int, str]` | `bool` | Like a video | YES
unlike_video() | `video_id: Union[int, str]` | `bool` | Unlike a video | YES
like_story() | `story_id: Union[int, str]` | `bool` | Like a story | YES
unlike_story() | `story_id: Union[int, str]` | `bool` | Unlike a story | YES
like_podcast() | `podcast_id: Union[int, str]` | `bool` | Like a podcast | YES
unlike_podcast() | `podcast_id: Union[int, str]` | `bool` | Unlike a podcast | YES

!> like methods return false if media had been liked already and unlike methods return false if media hadn't been liked before.

### Follow & Unfollow

Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
follow_artist() | `name: str` | `bool` | Follow a artist | YES
unfollow_artist() | `name: str` | `bool` | Unfollow a artist | YES
follow_user() | `username: str` | `bool` | Follow a user | YES
unfollow_user() | `username: str` | `bool` | Unfollow a user | YES
follow_music_playlist() | `id: str` | `bool` | Follow a music (song or mp3) playlist | YES
unfollow_music_playlist() | `id: str` | `bool` | Unfollow a music (song or mp3) playlist | YES

!> Pass exact artist name (on RJ api) as name 

### Work with playlists
- Create, rename or delete playlist
- Add song or video to playlist
- Remove song or video from playlist

Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
create_music_playlist() | <ul><li>`name: str`</li><br/><li>`song_id: Union[int, str]`</li></ul> | `str` | Create a music playlist and returns playlist id | YES
create_video_playlist() | <ul><li>`name: str`</li><br/><li>`video_id: Union[int, str]`</li></ul> | `str` | Create a video playlist and returns playlist id | YES
rename_music_playlist() | <ul><li>`id: str`</li><br/><li>`name: str`</li></ul> | `bool` | Rename your music playlist | YES
rename_video_playlist() | <ul><li>`id: str`</li><br/><li>`name: str`</li></ul> | `bool` | Rename your video playlist | YES
delete_music_playlist() | `id: str` | `bool` | Delete your music playlist | YES
delete_video_playlist() | `id: str` | `bool` | Delete your video playlist | YES
add_to_music_playlist() | <ul><li>`id: str`</li><br/><li>`song_id: Union[int, str]`</li></ul> | `bool` | Add a song to your music playlist | YES
add_to_video_playlist() | <ul><li>`id: str`</li><br/><li>`video_id: Union[int, str]`</li></ul> | `bool` | Add a video to your video playlist | YES
remove_from_music_playlist() | <ul><li>`id: str`</li><br/><li>`song_id: Union[int, str]`</li></ul> | `bool` | Remove a song from your music playlist | YES
remove_from_video_playlist() | <ul><li>`id: str`</li><br/><li>`video_id: Union[int, str]`</li></ul> | `bool` | Remove a video from your video playlist | YES

!> In RadioJavan you can't create empty playlist , so you need a song/video id for creating playlist.

!> **Add methods**: returns false if song/video had been added already\
**Remove methods**: returns false if song/video hadn't been added before

## Get Info
Get medias & users info as their [models](models).

> All methods work with out authentication too.

### Song <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_song_by_url() | `url: HttpUrl` | [Song](models?id=song) | Returns song info by site url (e.g. `radiojavan.com/mp3s/mp3/...`) | NO
get_song_by_id() | `id: Union[int, str]` | [Song](models?id=song) | Returns song info by id | NO


### Video <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_video_by_url() | `url: HttpUrl` | [Video](models?id=video) | Returns video info by site url (e.g. `radiojavan.com/videos/video/...`) | NO
get_video_by_id() | `id: Union[int, str]` | [Video](models?id=video) | Returns video info by id | NO

### Story <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_story_by_url() | `url: HttpUrl` | [Story](models?id=story) | Returns story info by site url (e.g. `radiojavan.com/story/...`) | NO
get_story_by_hash_id() | `hash_id: str` | [Story](models?id=story) | Returns story by hash id | NO

### Podcast <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_podcast_by_url() | `url: HttpUrl` | [Podcast](models?id=podcast) | Returns podcast info by site url (e.g. `radiojavan.com/podcasts/podcast/...`) | NO
get_podcast_by_id() | `id: Union[int, str]` | [Podcast](models?id=podcast) | Returns podcast info by id | NO

### Album <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_album_by_url() | `url: HttpUrl` | [Album](models?id=album) | Returns album info by site url (e.g. `radiojavan.com/mp3s/album/...`) | NO
get_album_by_id() | `id: Union[int, str]` | [Album](models?id=album) | Returns album info by id | NO

!> This id belong to one of album-tracks, usually first track.

### Artist <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_artist_by_url() | `url: HttpUrl` | [Artist](models?id=artist) | Returns artist info by site url (e.g. `radiojavan.com/artist/...`) | NO
get_artist_by_name() | `name: str` | [Artist](models?id=artist) | Returns artist info by id | NO

### Playlist <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_music_playlist_by_url() | `url: HttpUrl` | [MusicPlaylist](models?id=musicplaylist) | Returns music playlist info by site url (e.g. `radiojavan.com/playlists/playlist/mp3/...`) | NO
get_music_playlist_by_id() | `id: str` | [MusicPlaylist](models?id=musicplaylist) | Returns music playlist info by id | NO
get_video_playlist_by_url() | `url: HttpUrl` | [VideoPlaylist](models?id=videoplaylist) | Returns video playlist info by site url (e.g. `radiojavan.com/playlists/playlist/video/...`) | NO
get_video_playlist_by_id() | `id: str` | [VideoPlaylist](models?id=videoplaylist) | Returns video playlist info by id | NO

### User <!-- {docsify-ignore} -->
Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
get_user_by_url() | `url: HttpUrl` | [User](models?id=user) | Returns user info by site url (e.g. `radiojavan.com/u/...`) | NO
get_user_by_username() | `username: str` | [User](models?id=user) | Returns user info by username | NO
get_user_followers() | `username: str` | `list[`[ShortUser](models?id=shortuser)`]` | Returns list of user followers | NO
get_user_following() | `username: str` | `list[`[ShortUser](models?id=shortuser)`]` | Returns list of user following | NO


## Search
Search on RadioJavan and get results as [SearchResults](models?id=searchresults).

> This method work with out authentication too.

Method | Arguments | Return | Description | Login Required
-------|----------|--------|-------------|--------------
search() | `query: str` | [SearchResults](models?id=searchresults) | Returns search results object | NO

## Browse
Everything you see in `Browse` tab in desktop application. like `trending`, `popular`, `featured`, `latest` and `...`.

> All methods work with out authentication too.

Method | Return | Description | Login Required
-------|--------|-------------|--------------
get_latest_stories() | `list[`[Story](models?id=story)`]` | Returns list of latest stories | NO
get_trending_songs() | `list[`[Song](models?id=song)`]` | Returns list of trending songs | NO
get_popular_songs() | `list[`[Song](models?id=song)`]` | Returns list of popular songs | NO
get_featured_songs() | `list[`[Song](models?id=song)`]` | Returns list of featured songs | NO
get_latest_albums() | `list[`[Album](models?id=album)`]` | Returns list of latest albums | NO
get_trending_videos() | `list[`[Video](models?id=video)`]` | Returns list of trending videos | NO
get_popular_videos() | `list[`[Video](models?id=video)`]` | Returns list of popular videos | NO
get_featured_videos() | `list[`[Video](models?id=video)`]` | Returns list of featured videos | NO
get_latest_videos() | `list[`[Video](models?id=video)`]` | Returns list of latest videos | NO
get_popular_podcasts() | `list[`[Podcast](models?id=podcast)`]` | Returns list of popular podcasts | NO
get_featured_podcasts() | `list[`[Podcast](models?id=podcast)`]` | Returns list of featured podcasts | NO
get_talk_podcasts() | `list[`[Podcast](models?id=podcast)`]` | Returns list of talk podcasts | NO
get_shows_podcasts() | `list[`[Podcast](models?id=podcast)`]` | Returns list of shows podcasts | NO
get_popular_artists() | `list[`[Artist](models?id=artist)`]` | Returns list of popular artists | NO


## Others
Get stream links and ... .

> All methods work with out authentication too.

Method | Return | Description | Login Required
-------|-----------|-------------|--------------
get_trending_searches() | `list[str]` | Returns list of trending searches | NO
get_tv_stream() | `str` | Returns RJ tv stream link | NO
get_radio_stream() | `dict` | Returns RJ radio stream links and short data of current and next songs | NO