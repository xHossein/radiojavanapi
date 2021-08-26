from radiojavanapi.helper import to_int
from radiojavanapi.models import (
            Account, Album, Artist, MyPlaylists,
            ShortUser, Song, MusicPlaylist, Story, User, Video,
            ShortData, Podcast, SearchResults, VideoPlaylist
            )

def extract_account(data) -> Account:
    data["default_thumbnail"] = data.pop('default_thumb')
    data["has_subscription"] = data.pop('subscription')
    data["has_custom_photo"] = data.pop('custom_photo')
    data["is_verified"] = data.pop('verify')
    data["artists_name"] = [artist["name"] for artist in data.pop('artists')]
    data["stories"] = [extract_story(story) 
                    for story in data.pop('selfies',[])]
    return Account(**data)

def extract_user(data) -> User:
    data["default_thumbnail"] = data.pop('default_thumb')
    data["has_custom_photo"] = data.pop('custom_photo')
    data["has_subscription"] = data.pop('subscription')
    data["is_verified"] = data.pop('verify')
    data["artists_name"] = [artist["name"] for artist in data.pop('artists')]
    data["stories"] = [extract_story(story) 
                    for story in data.pop('selfies',[])]
    data["music_playlists"] = [extract_short_data(playlist['playlist'], MusicPlaylist)
                                for playlist in data.pop('playlists')]
    return User(**data)

def extract_song(data) -> Song:
    album = data.pop('album', None)
    if type(album) == dict:
        album = album.pop('album', None)
    data["album"] = album if album else data.pop('album', None)
    data["plays"] = to_int(data.pop('plays'))
    data["name"] = data.pop('song')
    data["likes"] = to_int(data.pop('likes'))
    data["dislikes"] = to_int(data.pop('dislikes'))
    data["downloads"] = to_int(data.pop('downloads'))
    data["related_songs"] = [extract_short_data(song, Song) for song in data.pop('related',[])]
    data["stories"] = [extract_story(story) for story in data.pop('selfies',[])]
    return Song(**data)

def extract_video(data) -> Video:
    data["lq_hls"] = data.get('low_web')
    data["hq_hls"] = data.get('high_web')
    data["name"] = data.pop('song')
    data["views"] = to_int(data.pop('views'))
    data["likes"] = to_int(data.pop('likes'))
    data["dislikes"] = to_int(data.pop('dislikes'))
    data["related_videos"] = [extract_short_data(video, Video) for video in data.pop('related',[])]
    return Video(**data)

def extract_podcast(data) -> Podcast:
    data["is_talk"] = data.pop('talk')
    data["plays"] = to_int(data.pop('plays'))
    data["likes"] = to_int(data.pop('likes'))
    data["dislikes"] = to_int(data.pop('dislikes'))
    data["related_podcasts"] = [extract_short_data(podcast, Podcast) for podcast in data.pop('related',[])]
    return Podcast(**data)

def extract_artist(data) -> Artist:
    data["photo_thumbnail"] = data.pop('photo_thumb')
    data["latest_song"] = extract_short_data(data.pop('latest'), Song) if data.get('latest') else None
    data['name'] = data.pop('query')
    followers = data.pop('followers')
    data["followers_count"] = followers['count']
    data["following"] = followers['following']
    data["plays"] = followers['plays']
    data["songs"] = [extract_short_data(mp3, Song) for mp3 in data.pop('mp3s')]
    data["albums"] = [extract_short_data(album, Album) for album in data.pop('albums')]
    data["videos"] = [extract_short_data(video, Video) for video in data.pop('videos')]
    data["podcasts"] = [extract_short_data(podcasts, Podcast) for podcasts in data.pop('podcasts')]
    data["music_playlists"] = [extract_short_data(playlist['playlist'], MusicPlaylist)
                                for playlist in data.pop('playlists')]
    return Artist(**data)

def extract_short_data(data, type) -> ShortData:
    if type == Song or type == Video:
        data["name"] = data["song"]
    
    elif type == Album:
        data["artist"] = data["album_artist"]
        data["name"] = data["album_album"]
      
    elif type == Podcast:
        data["artist"] = data["podcast_artist"]
        data["name"] = data["title"]  
        data["title"] = '{} - \"{}\"'.format(data["artist"], data["name"])
        
    elif type == MusicPlaylist:
        data["name"] = data["title"]
        data["title"] = '{} - \"{}\"'.format(data["name"], data["created_by"])
        
    elif type == VideoPlaylist:
        data["name"] = data["title"]
        
    elif type == 'show':
        data["artist"] = data["date"]
        data["name"] = data["show_title"]
        data["title"] = '{} - \"{}\"'.format(data["artist"], data["name"])
        data["permlink"] = data["show_permlink"]
        
    return ShortData(**data)

def extract_search_results(data) -> SearchResults:
    data["songs"] = [extract_short_data(mp3, Song) for mp3 in data.pop('mp3s')]
    data["albums"] = [extract_short_data(album, Album) for album in data.pop('albums')]
    data["videos"] = [extract_short_data(video, Video) for video in data.pop('videos')]
    data["podcasts"] = [extract_short_data(podcasts, Podcast) for podcasts in data.pop('podcasts')]
    data["shows"] = [extract_short_data(show, 'show') for show in data.pop('shows')]
    data["users"] = [extract_short_user(profile) for profile in data.pop('profiles')]
    data["artist_names"] = [artist["name"] for artist in data.pop('artists')]
    data["music_playlists"] = [extract_short_data(playlist['playlist'], MusicPlaylist)
                                                    for playlist in data.pop('playlists')]
    return SearchResults(**data)

def extract_video_playlist(data) -> VideoPlaylist:
    data['is_my_playlist'] = data.pop('myplaylist')
    data["videos"] = [extract_video(video) for video in data.pop('items',[])]
    return VideoPlaylist(**data)

def extract_music_playlist(data) -> MusicPlaylist:
    data['is_my_playlist'] = data.pop('myplaylist')
    data['is_public'] = data.pop('public')
    data['has_custom_photo'] = data.pop('custom_photo')
    data["sync"] = True if data.pop('sync', None) else False
    data["songs"] = [extract_song(song) for song in data.pop('items',[])]
    return MusicPlaylist(**data)

def extract_short_user(data) -> Story:
    return ShortUser(**data)

def extract_story(data) -> Story:
    data['is_verified'] = data.pop('verified')
    data['lq_link'] = data.pop('hls')
    data["song_id"] = data.pop('mp3')
    data['is_my_story'] = data.pop('myselfie',None)
    data['user'] = extract_short_user(data.pop('user'))
    return Story(**data)

def extract_album(data):
    data["tracks"] = [extract_song(song) 
                    for song in data.pop('album_tracks')]
    data['name'] = data.pop('album_album')
    data['artist'] = data.pop('album_artist')
    data['share_link'] = data.get('album_share_link','share_link')
    return Album(**data)

def extract_my_playlists(data):
    return MyPlaylists(**{
                "music_playlists": [extract_short_data(mpl, MusicPlaylist)
                                    for mpl in data['mp3s']['myplaylists']],
                "video_playlists": [extract_short_data(vpl, VideoPlaylist)
                                    for vpl in data['videos']['myplaylists']]
                })

