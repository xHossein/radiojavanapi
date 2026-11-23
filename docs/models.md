# Models

## Account
This model represents your account on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on an Account object

Example:

```python
account.email
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | Your account name
`firstname` | `str` | Your account first name
`lastname` | `str` | Your account last name
`display_name` | `str` | The name other users see
`username` | `str` | Your account username
`email` | `str` | Your account email
`bio` | `Optional[str]` | Your account bio
`share_link` | `HttpUrl` | Your profile URL
`has_subscription` | `bool` | Subscription status
`has_custom_photo` | `bool` | `True` when you have a profile photo
`is_verified` | `bool` | Verification status
`default_photo` | `HttpUrl` | Default photo URL
`default_thumbnail` | `HttpUrl` | Default thumbnail URL
`photo` | `HttpUrl` | Current photo URL
`thumbnail` | `HttpUrl` | Thumbnail URL
`followers_count` | `str` | Followers count
`following_count` | `str` | Following count
`playlists_count` | `int` | Number of playlists in your library
`songs_count` | `int` | Number of songs in your library
`artists_count` | `int` | Number of artists you follow
`artists_name` | `list[str]` | Names of the artists you follow
`stories` | `list[`[Story](#story)`]` | Stories you've uploaded on RJ

## Song
This model represents a song (mp3) on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Song object

Example:

```python
song.dislikes
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
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`share_link` | `HttpUrl` | Song URL
`title` | `str` | Title
`credits` | `Optional[str]` | Credits
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | Dislikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High-quality download link
`lq_link` | `HttpUrl` | Low-quality download link
`hls_link` | `Optional[HttpUrl]` | Stream link
`hq_hls` | `Optional[HttpUrl]` | High-quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low-quality stream link
`album` | `Optional[str]` | Album name
`date` | `Optional[str]` | Release date (the RJ API usually omits this)
`duration` | `float` | Song duration in seconds
`thumbnail` | `HttpUrl` | Thumbnail URL
`lyric` | `Optional[str]` | Song lyrics
`related_songs` | `list[`[ShortData](#shortdata)`]` | Related songs
`stories` | `list[`[Story](#story)`]` | Stories that use this song

## Video
This model represents a video on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Video object

Example:

```python
video.dislikes
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
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`share_link` | `HttpUrl` | Video URL
`title` | `str` | Title
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | Dislikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High-quality download link
`lq_link` | `HttpUrl` | Low-quality download link
`hq_hls` | `Optional[HttpUrl]` | High-quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low-quality stream link
`date` | `Optional[str]` | Release date (the RJ API usually omits this)
`related_videos` | `list[`[ShortData](#shortdata)`]` | Related videos

## Album
This model represents an album on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on an Album object

Example:

```python
album.tracks
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `Union[str, int]` | Album id
`name` | `str` | Album name
`artist` | `str` | Album artist
`created_at` | `str` | Date and time the album was posted
`date` | `str` | Release date (the RJ API usually omits this)
`tracks` | `list[`[Song](#song)`]` | All tracks
`share_link` | `HttpUrl` | Album URL

## Podcast
This model represents a podcast on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Podcast object

Example:

```python
podcast.duration
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Podcast id
`plays` | `int` | Plays count
`created_at` | `str` | Date and time the podcast was posted
`permlink` | `str` | Podcast permlink
`show_permlink` | `str` | Usually the same as `permlink`
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`share_link` | `HttpUrl` | Podcast URL
`title` | `str` | Title
`credit_tags` | `list[str]` | Credit tags
`likes` | `int` | Likes count
`dislikes` | `int` | Dislikes count
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High-quality download link
`lq_link` | `HttpUrl` | Low-quality download link
`hls_link` | `Optional[HttpUrl]` | Stream link
`hq_hls` | `Optional[HttpUrl]` | High-quality stream link
`lq_hls` | `Optional[HttpUrl]` | Low-quality stream link
`is_talk` | `bool` | `True` if this is a talk podcast
`date` | `str` | Release date
`short_date` | `str` | Same as `date`
`duration` | `float` | Episode duration in seconds
`thumbnail` | `HttpUrl` | Thumbnail URL
`tracklist` | `Optional[str]` | Podcast track list (newline-separated text)
`tracklist_synced` | `list[`[PodcastTrackSync](#podcasttracksync)`]` | Time-synced track list
`related_podcasts` | `list[`[ShortData](#shortdata)`]` | Related podcasts

## PodcastTrackSync
This model represents one entry in a podcast's time-synced track list.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a PodcastTrackSync object

Available attributes:

| Name | Type | Description
-------|------|------------
`time` | `int` | Start time of the track, in seconds
`text` | `str` | Track title
`mp3` | `Optional[int]` | Id of the matching song, if any

## Artist
This model represents an artist on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on an Artist object

Example:

```python
artist.name
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | Artist name
`plays` | `str` | Plays count (e.g. `2M`)
`photo` | `HttpUrl` | Photo URL
`photo_player` | `HttpUrl` | Player photo URL
`photo_thumbnail` | `HttpUrl` | Thumbnail URL
`background` | `HttpUrl` | Background photo URL
`share_link` | `HttpUrl` | Artist URL
`following` | `bool` | `True` if you follow this artist
`followers_count` | `int` | Artist followers count
`prereleases` | `list` | Prerelease items
`events` | `list` | Events
`photos` | `list` | Photos
`latest_song` | `Optional[`[ShortData](#shortdata)`]` | Latest song
`songs` | `list[`[ShortData](#shortdata)`]` | Artist songs
`albums` | `list[`[ShortData](#shortdata)`]` | Artist albums
`videos` | `list[`[ShortData](#shortdata)`]` | Artist videos
`podcasts` | `list[`[ShortData](#shortdata)`]` | Artist podcasts
`music_playlists` | `list[`[ShortData](#shortdata)`]` | Artist music (song/mp3) playlists


## Story
This model represents a story (selfie) on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a Story object

Example:

```python
story.id
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `int` | Story id
`hash_id` | `str` | Story hash id
`title` | `str` | Story title
`location` | `str` | Story location
`song` | `str` | Name of the song in the story
`song_id` | `int` | Id of the song in the story
`artist` | `str` | Song artist name
`link` | `HttpUrl` | Download link
`hq_link` | `HttpUrl` | High-quality download link
`lq_link` | `HttpUrl` | Low-quality download link
`filename` | `str` | File name
`share_link` | `HttpUrl` | Story URL
`photo` | `HttpUrl` | Photo URL
`thumbnail` | `HttpUrl` | Thumbnail URL
`is_verified` | `bool` | Verification status of the owner
`likes` | `str` | Story likes count
`likes_pretty` | `str` | Story likes count in a pretty format
`user` | [ShortUser](#shortuser) | The owner of the story
`is_my_story` | `bool` | `True` if you are the owner

## User
This model represents a user on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a User object

Example:

```python
user.music_playlists
```

Available attributes:

| Name | Type | Description
-------|------|------------
`name` | `str` | User's name
`firstname` | `str` | User's first name
`lastname` | `str` | User's last name
`display_name` | `str` | The name other users see
`username` | `str` | User's username
`bio` | `Optional[str]` | User's bio
`share_link` | `HttpUrl` | User profile URL
`has_subscription` | `bool` | Subscription status
`has_custom_photo` | `bool` | `True` when the user has a profile photo
`is_verified` | `bool` | Verification status
`default_photo` | `HttpUrl` | Default photo URL
`default_thumbnail` | `HttpUrl` | Default thumbnail URL
`photo` | `HttpUrl` | Current photo URL
`thumbnail` | `HttpUrl` | Thumbnail URL
`followers_count` | `str` | Followers count
`following_count` | `str` | Following count
`following` | `bool` | `True` if you follow this user
`playlists_count` | `int` | Number of playlists the user has
`songs_count` | `int` | Number of songs in the user's library
`artists_count` | `int` | Number of artists the user follows
`artists_name` | `list[str]` | Names of the artists the user follows
`stories` | `list[`[Story](#story)`]` | Stories the user has uploaded on RJ
`music_playlists` | `list[`[ShortData](#shortdata)`]` | User's music (mp3) playlists

## ShortUser
This model represents a user with only a small amount of data. To get the full data, call a [Get Info](methods?id=get-info) method with the user's username.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a ShortUser object

Example:

```python
short_user.display_name
```

Available attributes:

| Name | Type | Description
-------|------|------------
`display_name` | `str` | The name other users see
`username` | `Optional[str]` | Username
`thumbnail` | `HttpUrl` | Thumbnail URL
`share_link` | `Optional[HttpUrl]` | Profile URL

## MusicPlaylist
This model represents a music (song/mp3) playlist on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a MusicPlaylist object

Example:

```python
playlist.songs
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `str` | Music playlist id
`title` | `str` | Title
`count` | `int` | Number of songs
`created_at` | `str` | Date and time the playlist was created
`created_by` | `str` | Owner of the playlist
`last_updated_at` | `str` | Date and time the playlist was last updated
`share_link` | `HttpUrl` | Playlist URL
`followers` | `int` | Followers count
`following` | `Optional[bool]` | `True` if you follow this playlist
`sync` | `Optional[bool]` | Sync status
`is_public` | `bool` | `True` if the playlist is public
`is_my_playlist` | `bool` | `True` if you own the playlist
`has_custom_photo` | `bool` | `True` when the playlist has a custom photo
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`thumbnail` | `HttpUrl` | Thumbnail URL
`songs` | `list[`[Song](#song)`]` | All songs in the playlist

## VideoPlaylist
This model represents a video playlist on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a VideoPlaylist object

Example:

```python
playlist.videos
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `str` | Video playlist id
`title` | `str` | Title
`count` | `int` | Number of videos
`created_at` | `str` | Date and time the playlist was created
`last_updated_at` | `str` | Date and time the playlist was last updated
`share_link` | `HttpUrl` | Playlist URL
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`thumbnail` | `HttpUrl` | Thumbnail URL
`is_my_playlist` | `bool` | `True` if you own the playlist
`videos` | `list[`[Video](#video)`]` | All videos in the playlist

## SearchResults
This model represents search results on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a SearchResults object

Example:

```python
results.songs
```

Available attributes:

| Name | Type | Description
-------|------|------------
`query` | `str` | The search query
`songs` | `list[`[ShortData](#shortdata)`]` | Songs found by the search
`albums` | `list[`[ShortData](#shortdata)`]` | Albums found by the search
`videos` | `list[`[ShortData](#shortdata)`]` | Videos found by the search
`podcasts` | `list[`[ShortData](#shortdata)`]` | Podcasts found by the search
`music_playlists` | `list[`[ShortData](#shortdata)`]` | Music (song/mp3) playlists found by the search
`shows` | `list[`[ShortData](#shortdata)`]` | Shows found by the search
`users` | `list[`[ShortUser](#shortuser)`]` | Users found by the search
`artist_names` | `list[str]` | Names of all artists found by the search


## ShortData
This model represents media with only a small amount of data. To get the full data, call a [Get Info](methods?id=get-info) method with the media's id or name.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a ShortData object

Example:

```python
short_data.id
```

Available attributes:

| Name | Type | Description
-------|------|------------
`id` | `Union[int, str]` | Media id
`artist` | `Optional[str]` | Name of the media's artist
`name` | `Optional[str]` | Name of the media
`created_at` | `str` | Date and time the media was posted
`permlink` | `Optional[str]` | Media permlink (e.g. `Donya-Boro-Bargard`)
`photo` | `HttpUrl` | Photo URL
`photo_player` | `Optional[HttpUrl]` | Player photo URL
`share_link` | `HttpUrl` | Media URL
`title` | `str` | Title

## MyPlaylists
This model represents your playlists on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a MyPlaylists object

Example:

```python
my_playlists.music_playlists
```

Available attributes:

| Name | Type | Description
-------|------|------------
`music_playlists` | `list[`[ShortData](#shortdata)`]` | Your music (song/mp3) playlists
`video_playlists` | `list[`[ShortData](#shortdata)`]` | Your video playlists


## NotificationsStatus
This model represents your current notification settings on RadioJavan.

### Attributes <!-- {docsify-ignore} -->
> Read-only values on a NotificationsStatus object

Example:

```python
notifications.artists_email
```

Available attributes:

| Name | Type | Description
-------|------|------------
`artists_email` | `bool` | Email notifications about followed artists
`artists_push` | `bool` | Push notifications about followed artists
`events_push` | `bool` | Push notifications about events
`music_email` | `bool` | Email notifications about new music
`music_push` | `bool` | Push notifications about new music
`playlists_followers_push` | `bool` | Push notifications about playlist followers
`selfies_push` | `bool` | Push notifications about stories