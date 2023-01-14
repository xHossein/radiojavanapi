# Models

## Account
This models your account on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Account object



Example:

```python
accountObj.email
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | Your account name
`firstname` | `str` | Your account firstname
`lastname` | `str` | Your account lastname
`display_name` | `str` | The name which shows to other users
`username` | `str` | Your account username
`email` | `str` | Your account email
`bio` | `Optional[str]` | Your account bio
`share_link` | `HttpUrl` | Your profile url
`has_subscription` | `bool` | Status of subscription
`has_custom_photo` | `bool` | Its true when you have profile photo
`is_verified` | `bool` | Status of verification
`default_photo` | `HttpUrl` | Default photo url
`default_thumbnail` | `HttpUrl` | Default thumbnail url
`photo` | `HttpUrl` | Current photo url
`thumbnail` | `HttpUrl` | Thumbnail url
`followers_count` | `int` | Followers count
`following_count` | `int` | Following count
`playlists_count` | `int` | Number of playlists you have in your library
`songs_count` | `int` | Number of songs you have in your library
`artists_count` | `int` | Number of artists you've followed
`artists_name` | `list[str]` | Name of artists you've followed
`stories` | `list[`[Story](#story)`]` | Stories you've uploaded on RJ

## Song
This models a song (mp3) on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Song object



Example:

```python
songObj.dislikes
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Song id
`name` | `str` | Song name
`artist` | `str` | Song artist name
`artist_tags` | `list[str]` | Song artist tags
`plays` | `int` | Plays count
`downloads` | `int` | Downloads count
`created_at` | `str` | Date and time the song was posted
`permlink` | `str` | Song permlink (e.g. `Donya-Boro-Bargard`)
`photo` | `HttpUrl` | Photo url
`photo_player` | `Optional[HttpUrl]` | Player photo url
`share_link` | `HttpUrl` | Song url
`title` | `str` | Title
`credits` | `Optional[str]` | Credits
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | DisLikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High quality download link
`lq_link` | `HttpUrl` | Low quality download link
`hls_link` | `Optional[HttpUrl]` | Stream link
`hq_hls` | `Optional[HttpUrl]` | High quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low quality stream link
`album` | `Optional[str]` | Album name
`date` | `Optional[str]` | IDK! RJ api sent everything except date!
`duration` | `float` | Song duration
`thumbnail` | `HttpUrl` | Thumbnail url
`lyric` | `Optional[str]` | Song lyric
`related_songs` | `list[`[ShortData](#shortdata)`]` | Related songs
`stories` | `list[`[Story](#story)`]` | Stories with that song

## Video
This models a video on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Video object



Example:

```python
videoObj.dislikes
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Video id
`name` | `str` | Video name
`artist` | `str` | Video artist name
`artist_tags` | `list[str]` | Video artist tags
`views` | `int` | Views count
`created_at` | `str` | Date and time the video was posted
`permlink` | `str` | Video permlink
`photo` | `HttpUrl` | Photo url
`photo_player` | `Optional[HttpUrl]` | Player photo url
`share_link` | `HttpUrl` | Video url
`title` | `str` | Title
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | DisLikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High quality download link
`lq_link` | `HttpUrl` | Low quality download link
`hq_hls` | `Optional[HttpUrl]` | High quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low quality stream link
`date` | `Optional[str]` | IDK! RJ api sent everything except date!
`related_videos` | `list[`[ShortData](#shortdata)`]` | Related videos

## Album
This models an album on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on an Album object



Example:

```python
albumObj.tracks
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `str` | Album id
`name` | `str` | Album name
`artist` | `str` | Album artist
`created_at` | `str` | Date and time the Album was posted
`date` | `str` | IDK! RJ api sent everything except date!
`tracks` | `list[`[Song](#song)`]` | All tracks
`share_link` | `HttpUrl` | Album url

## Podcast
This models a podcast on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Podcast object



Example:

```python
podcastObj.duration
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Podcast id
`plays` | `int` | Plays count
`created_at` | `str` | Date and time the podcast was posted
`permlink` | `str` | Podcast permlink
`show_permlink` | `str` | In many times its equal to `permlink`
`photo` | `HttpUrl` | Photo url
`photo_player` | `Optional[HttpUrl]` | Player photo url
`share_link` | `HttpUrl` | Podcast url
`title` | `str` | Title
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | DisLikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High quality download link
`lq_link` | `HttpUrl` | Low quality download link
`hls_link` | `Optional[HttpUrl]` | Stream link
`hq_hls` | `Optional[HttpUrl]` | High quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low quality stream link
`is_talk` | `bool` | Its true if it is a talk-podcast
`date` | `str` | IDK! RJ api sent everything except date!
`short_date` | `str` | Same as `date`
`duration` | `float` | Song duration
`thumbnail` | `HttpUrl` | Thumbnail url
`tracklist` | `Optional[str]` | Podcast track list (contains new line `\n`)
`related_podcasts` | `list[`[ShortData](#shortdata)`]` | Related podcasts

## Artist
This models an artist on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on an Artist object



Example:

```python
artistObj.name
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | Artist name
`plays` | `str` | Plays count (e.g. `2M`)
`photo` | `HttpUrl` | Photo url
`photo_player` | `HttpUrl` | Player photo url
`photo_thumb` | `HttpUrl` | Thumbnail url
`background` | `HttpUrl` | Background photo url
`share_link` | `HttpUrl` | Artist url
`following` | `bool` | Its true if you following that artist
`followers_count` | `int` | Artist followers count
`prereleases` | `Optional[list]` | Prereleases items
`events` | `Optional[list]` | Events
`photos` | `Optional[list]` | Photos
`latest_song` | `list[`[ShortData](#shortdata)`]` | Latest song
`songs` | `list[`[ShortData](#shortdata)`]` | Artist songs
`albums` | `list[`[ShortData](#shortdata)`]` | Artist albums
`videos` | `list[`[ShortData](#shortdata)`]` | Artist videos
`podcasts` | `list[`[ShortData](#shortdata)`]` | Artist podcasts
`music_playlists` | `list[`[ShortData](#shortdata)`]` | Artist song (mp3) playlist


## Story
This models a story (selfie) on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Story object



Example:

```python
storyObj.id
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Story id
`hash_id` | `str` | Story hash id
`title` | `str` | Story title
`location` | `str` | Story location
`song` | `str` | Name of song in story
`song_id` | `int` | Id of song in story
`artist` | `str` | Song artist name
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High quality download link
`lq_link` | `HttpUrl` | Low quality download link
`filename` | `str` | File name
`share_link` | `HttpUrl` | Story url
`photo` | `HttpUrl` | Photo url
`thumbnail` | `HttpUrl` | Thumbnail url
`is_verified` | `bool` | Status of user or story verification
`likes` | `str` | Story likes count
`likes_pretty` | `str` | Story likes count in pretty format
`user` | `list[`[User](#user)`]` | The owner of story
`is_my_story` | `bool` | Its true if you are the owner

## User
This models a user on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a User object



Example:

```python
userObj.tracks
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | User's name
`firstname` | `str` | User's firstname
`lastname` | `str` | User's lastname
`display_name` | `str` | The name which shows to other users
`username` | `str` | User's username
`bio` | `Optional[str]` | User's bio
`share_link` | `HttpUrl` | User profile url
`has_subscription` | `bool` | Status of subscription
`has_custom_photo` | `bool` | Its true when user has profile photo
`is_verified` | `bool` | Status of verification
`default_photo` | `HttpUrl` | Default photo url
`default_thumbnail` | `HttpUrl` | Default thumbnail url
`photo` | `HttpUrl` | Current photo url
`thumbnail` | `HttpUrl` | Thumbnail url
`followers_count` | `int` | Followers count
`following_count` | `int` | Following count
`following` | `Optional[bool]` | Its true if you following this user
`playlists_count` | `int` | Number of playlists user has
`songs_count` | `int` | Number of songs user has in library
`artists_count` | `int` | Number of artists user has followed
`artists_name` | `list[str]` | Name of artists user has followed
`stories` | `list[`[Story](#story)`]` | Stories user has uploaded on RJ
`music_playlists` | `list[`[ShortData](#shortdata)`]` | User music (mp3) playlists

## ShortUser
This models a user with small data. To get full data you must use [Get Info](methods?id=get-info) methods with User's username.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a ShortUser object



Example:

```python
shortuserObj.tracks
```

Available attributes:

| Name | Type | Description
-------|------|------------
`display_name` | `str` | The name which users see
`username` | `str` | Username
`thumbnail` | `HttpUrl` | Thumbnail url
`share_link` | `Optional[HttpUrl]` | Thumbnail url

## MusicPlaylist
This models a music (song or mp3) playlist on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a MusicPlaylist object



Example:

```python
playlistObj.songs
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `str` | MusicPlaylist id
`title` | `str` | Title
`count` | `int` | Songs count
`created_at` | `str` | Date and time the playlist was created
`created_by` | `str` | Owner of playlist
`last_updated_at` | `str` | Latest date and time the playlist was updated
`share_link` | `HttpUrl` | Playlist url
`followers` | `int` | Followers count
`following` | `Optional[bool]` | Its true if you following that playlist
`sync` | `Optional[bool]` | Sync
`is_public` | `bool` | Its true if its a public playlist
`is_my_playlist` | `bool` | Its true if you are the owner
`has_custom_photo` | `bool` | Its true when it has a custom photo
`photo` | `HttpUrl` | Photo url
`photo_player` | `Optional[HttpUrl]` | Player photo url
`thumbnail` | `HttpUrl` | Thumbnail url
`songs` | `list[`[Song](#song)`]` | All songs which in playlist

## VideoPlaylist
This models a video playlist on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a VideoPlaylist object



Example:

```python
playlistObj.videos
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `str` | VideoPlaylist id
`title` | `str` | Title
`count` | `int` | Videos count
`created_at` | `str` | Date and time the playlist was created
`last_updated_at` | `str` | Latest date and time the playlist was updated
`share_link` | `HttpUrl` | Playlist url
`photo` | `HttpUrl` | Photo url
`photo_player` | `Optional[HttpUrl]` | Player photo url
`thumbnail` | `HttpUrl` | Thumbnail url
`is_my_playlist` | `bool` | Its true if you are the owner
`videos` | `list[`[Video](#video)`]` | All videos which in playlist

## SearchResults
This models a search results on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a SearchResults object



Example:

```python
resultsObj.songs
```

Available attributes:

| Name | Type | Description
-------|------|------------
`query` | `str` | Query
`songs` | `list[`[ShortData](#shortdata)`]` | All songs which found by search
`albums` | `list[`[ShortData](#shortdata)`]` | All albums which found by search
`videos` | `list[`[ShortData](#shortdata)`]` | All videos which found by search
`podcasts` | `list[`[ShortData](#shortdata)`]` | All podcasts which found by search
`music_playlists` | `list[`[ShortData](#shortdata)`]` | All song (mp3) playlists which found by search
`shows` | `list[`[ShortData](#shortdata)`]` | All shows which found by search
`users` | `list[`[User](#user)`]` | All users which found by search
`artist_names` | `list[str]` | Name of all artists which found by search


## ShortData
This models medias with small data. To get full data you must use [Get Info](methods?id=get-info) methods with id or name.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a ShortData object



Example:

```python
shordataObj.id
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `Union[int, str]` | Media id
`artist` | ` Optional[str]` | Name of media artist 
`name` | ` Optional[str]` | Name of media
`created_at` | `str` | Date and time that the media was posted
`permlink` | ` Optional[str]` | Media permlink (e.g. `Donya-Boro-Bargard`)
`photo` | `HttpUrl` | Photo url
`photo_player` | `HttpUrl` | Player photo url
`share_link` | `HttpUrl` | Media url
`title` | `str` | Title

## MyPlaylists
This models your playlists on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a MyPlaylists object



Example:

```python
myplaylistsObj.music_playlists
```

Available attributes:

| Name | Type | Description
-------|------|------------
`music_playlists` | `list[`[ShortData](#shortdata)`]` | Your song (mp3) playlists
`video_playlists` | `list[`[ShortData](#shortdata)`]` | Your video plyalists


## NotificationsStatus
This models your current status of notifications settings on RadioJavan.


### Attributes <!-- {docsify-ignore} -->
> Read-only values on a NotificationsStatus object



Example:

```python
notifObj.artists_email
```

Available attributes:

| Name | Type 
-------|------
`artists_email` | `bool`
`artists_push` | `bool`
`events_push` | `bool`
`music_email` | `bool`
`music_push` | `bool`
`playlists_followers_push` | `bool` 
`selfies_push` | `bool` 