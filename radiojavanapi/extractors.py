from radiojavanapi.helper import toInt
from .types import (Account, Album, Artist, ComingSoon, Profile,
                    Song, MusicPlaylist, Story, Video,
                    Podcast,SearchResults,VideoPlaylist)

def extract_account(data) -> Account:
    data["artists_name"] = [artist["name"] for artist in data.pop('artists')]
    data["stories"] = [extract_story(story) 
                    for story in data.pop('selfies',[])]
    return Account(**data)

def extract_song(data) -> Song:
    album_dic = data.pop('album',None)
    album_str = data.pop('album_album',None)
    data["album"] = album_dic['album'] if album_dic else album_str
    data["plays"] = toInt(data.pop('plays'))
    data["likes"] = toInt(data.pop('likes'))
    data["dislikes"] = toInt(data.pop('dislikes'))
    data["downloads"] = toInt(data.pop('downloads'))
    data["related_songs_id"] = [song["id"] for song in data.pop('related',[])]
    data["stories"] = [extract_story(story) 
                    for story in data.pop('selfies',[])]
    return Song(**data)

def extract_video(data) -> Video:
    data["lq_hls"] = data.get('low_web')
    data["hq_hls"] = data.get('high_web')
    data["views"] = toInt(data.pop('views'))
    data["likes"] = toInt(data.pop('likes'))
    data["dislikes"] = toInt(data.pop('dislikes'))
    data["related_video_id"] = [video["id"] for video in data.pop('related',[])]
    return Video(**data)

def extract_podcast(data) -> Podcast:
    data["plays"] = toInt(data.pop('plays'))
    data["likes"] = toInt(data.pop('likes'))
    data["dislikes"] = toInt(data.pop('dislikes'))
    data["related_podcast_id"] = [podcast["id"] for podcast in data.pop('related',[])]
    return Podcast(**data)

def extract_artist(data) -> Artist:
    data["latest_song_id"] = data.pop('latest')['id'] if data.get('latest') else None
    data['name'] = data.pop('query')
    followers = data.pop('followers')
    data["followers_count"] = followers['count']
    data["following"] = followers['following']
    data["plays"] = followers['plays']
    data["songs_id"] = [mp3["id"] for mp3 in data.pop('mp3s')]
    data["albums_id"] = [album["id"] for album in data.pop('albums')]
    data["videos_id"] = [video["id"] for video in data.pop('videos')]
    data["podcasts_id"] = [podcasts["id"] for podcasts in data.pop('podcasts')]
    data["playlists_id"] = [playlist["playlist"]["id"] 
                            for playlist in data.pop('playlists')]
    return Artist(**data)

def extract_search_results(data) -> SearchResults:
    data["songs_id"] = [mp3["id"] for mp3 in data.pop('mp3s')]
    data["albums_id"] = [album["id"] for album in data.pop('albums')]
    data["videos_id"] = [video["id"] for video in data.pop('videos')]
    data["podcasts_id"] = [podcasts["id"] for podcasts in data.pop('podcasts')]
    data["playlists_id"] = [playlist["playlist"]["id"] 
                            for playlist in data.pop('playlists')]
    data["artists_name"] = [artist["name"] for artist in data.pop('artists')]
    return SearchResults(**data)

def extract_video_playlist(data) -> VideoPlaylist:
    data["videos"] = [extract_video(video) for video in data.pop('items',[])]
    return VideoPlaylist(**data)

def extract_music_playlist(data) -> MusicPlaylist:
    data["sync"] = True if data.pop('sync') else False
    data["songs"] = [extract_song(song) for song in data.pop('items',[])]
    return MusicPlaylist(**data)

def extract_profile(data) -> Story:
    return Profile(**data)

def extract_story(data) -> Story:
    data['lq_link'] = data.pop('hls')
    data["song_id"] = data.pop('mp3')
    data['is_mystory'] = data.pop('myselfie',None)
    data['user'] = extract_profile(data.pop('user'))
    return Story(**data)

def extract_coming_soon(data):
    return ComingSoon(**data)

def extract_album(data):
    data["tracks"] = [extract_song(song) 
                    for song in data.pop('album_tracks')]
    data['album'] = data.pop('album_album')
    data['artist'] = data.pop('album_artist')
    data['share_link'] = data.get('album_share_link','share_link')
    return Album(**data)

