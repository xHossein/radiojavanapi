from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class Profile(BaseModel):
    thumbnail: HttpUrl
    username: Optional[str]
    display_name: str

class Story(BaseModel):
    id: int
    hash_id: str
    title: str
    song: str
    song_id: int
    artist: str
    link: HttpUrl
    lq_link: HttpUrl
    hq_link: HttpUrl
    filename: str
    share_link: HttpUrl
    photo: HttpUrl
    thumbnail: HttpUrl
    verified: bool
    type: str
    likes: str
    likes_pretty: str
    user: Profile
    location: str
    is_mystory: Optional[bool]

class Account(BaseModel):
    name: str
    firstname: str
    lastname: str
    display_name: str
    username: str
    share_link: HttpUrl
    email: str
    has_subscription : bool
    custom_photo : bool
    photo: HttpUrl
    thumbnail: HttpUrl
    playlists_count: int
    songs_count: int
    artists_count : int
    artists_name: List[str] = []
    stories: List[Story] = []

class RJBaseModel(BaseModel):
    comments_link: HttpUrl
    created_at: str
    credit_tags: List[str] = []
    dislikes: int
    hq_hls: Optional[HttpUrl]
    hq_link: HttpUrl
    id: int
    likes: int
    link: HttpUrl
    lq_hls: Optional[HttpUrl]
    lq_link: HttpUrl
    permlink: str
    photo: HttpUrl
    photo_player: HttpUrl
    share_link: HttpUrl
    title: str
    type: str

class Song(RJBaseModel):
    artist: str
    song: str
    item: Optional[str] # for playlist
    album: Optional[str]
    date: Optional[str]
    duration: float
    hls_link: Optional[HttpUrl]
    thumbnail: HttpUrl
    plays: int
    downloads: int
    credits: Optional[str]
    artist_tags: List[str] = []
    lyric: Optional[str]
    related_songs_id: List[int] = []
    stories: List[Story] = []

class Video(RJBaseModel):
    artist: str
    song: str
    item: Optional[str] # for playlist
    date: Optional[str]
    views: int
    artist_tags: List[str] = []
    related_video_id: List[int] = []

class Podcast(RJBaseModel):
    date: str
    short_date: str
    talk: bool
    duration: float
    hls_link: Optional[HttpUrl]
    thumbnail: HttpUrl
    plays: int
    show_permlink: Optional[str]
    tracklist: Optional[str]
    related_podcast_id: List[int] = []

class Artist(BaseModel):
    name: str
    background: HttpUrl
    photo: HttpUrl
    photo_player: HttpUrl
    photo_thumb: HttpUrl
    share_link: HttpUrl
    prereleases: List = []
    events: List = []
    photos: List = []
    latest_song_id: Optional[int]
    followers_count: int
    following: bool
    plays: str
    songs_id: List[int] = []
    albums_id: List[int] = []
    videos_id: List[int] = []
    podcasts_id: List[int] = []
    playlists_id: List[str] = []

class SearchResults(BaseModel):
    query: str
    songs_id: List[int] = []
    albums_id: List[int] = []
    videos_id: List[int] = []
    podcasts_id: List[int] = []
    playlists_id: List[str] = []
    artists_name: List[str] = []
    lyrics: List = []
    shows: List = []
    profiles: List = []

class MusicPlaylist(BaseModel):
    id: str
    title: str
    count: int
    created_at: str
    created_by: str
    last_updated_at: str
    type: str
    subtype: str
    share_link: HttpUrl
    followers: int
    following: bool
    sync: bool
    public: bool
    myplaylist: bool
    photo: HttpUrl
    custom_photo: bool
    photo_player: HttpUrl
    thumbnail: HttpUrl
    songs: List[Song] = []

class VideoPlaylist(BaseModel):
    id: str
    title: str
    count: int
    created_at: str
    last_updated_at: str
    type: str
    subtype: str
    share_link: HttpUrl
    myplaylist: bool
    photo: HttpUrl
    photo_player: HttpUrl
    thumbnail: HttpUrl
    videos: List[Video] = []

class Album(BaseModel):
    id: str
    created_at: str
    date: str
    tracks: List[Song] = []
    album: str
    artist: str
    share_link: HttpUrl

class ComingSoon(BaseModel):
    song: str
    artist: str
    type: str
    link: HttpUrl
    share_link: HttpUrl
    html_link: HttpUrl
    photo: HttpUrl





