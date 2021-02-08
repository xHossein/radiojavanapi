from typing import Optional
from radiojavanapi.helper import url_to_id
from radiojavanapi.types import MusicPlaylist, Song, Video, VideoPlaylist
from pydantic import HttpUrl
from radiojavanapi.extractors import extract_video_playlist,extract_music_playlist
from radiojavanapi.mixins.private import PrivateRequest

class MusicPlayListMixin(PrivateRequest):
    def get_music_playlist_by_url(self,url:HttpUrl) -> MusicPlaylist:
        """
        Get music playlist info by site url (e.g. radiojavan.com/playlists/playlist/mp3/...)

        Parameters
        ----------
            url: Site url of music playlist

        Returns
        -------
            MusicPlaylist: An object of Music Playlist type

        """
        return self.get_music_playlist_by_id(url_to_id(url))

    def get_music_playlist_by_id(self,id:str) -> MusicPlaylist:
        """
        Get music playlist info by id

        Parameters
        ----------
            id: Unique id of music playlist

        Returns
        -------
            MusicPlaylist: An object of Music Playlist type

        """
        response = self.private_request('mp3_playlist_with_items',
                                        params=f'id={id}').json()
        return extract_music_playlist(response)

    def follow_music_playlist(self,music_playlist:MusicPlaylist) -> bool:
        """
        Follow a music playlist

        Parameters
        ----------
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        response = self.private_request('mp3_playlist_follow',
                                params=f'id={music_playlist.id}&type=mp3',
                                need_login=True).json()
        return True if response['success'] else False

    def unfollow_music_playlist(self,music_playlist:MusicPlaylist) -> bool:
        """
        UnFollow a music playlist

        Parameters
        ----------
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        response = self.private_request('mp3_playlist_unfollow',
                                params=f'id={music_playlist.id}&type=mp3',
                                need_login=True).json()
        return True if response['success'] else False

    def create_music_playlist(self,name:str,song:Song) -> Optional[str]:
        """
        Create a music playlist
        Note: in RJ you can't create empty playlist , so you need a song for creation playlist

        Parameters
        ----------
            name: Name of playlist
            song: An object of Song type

        Returns
        -------
            str: playlist's id

        """
        response = self.private_request('mp3_playlist_add',
                                params=f'type=mp3&mp3={song.id}&name={name}',
                                need_login=True).json()
        return response['playlist'] if response['success'] else None

    def delete_music_playlist(self,music_playlist:MusicPlaylist) -> bool:
        """
        Delete your music playlist

        Parameters
        ----------
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        return self.private_request('mp3_playlist_remove',
                        params=f'type=mp3&id={music_playlist.id}',
                        need_login=True).json()['success']

    def rename_music_playlist(self,music_playlist:MusicPlaylist,new_name:str) -> bool:
        """
        Rename your music playlist

        Parameters
        ----------
            new_name: The name you want to set for a playlist
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        return self.private_request('mp3_playlist_rename',
                    params=f'type=mp3&id={music_playlist.id}&name={new_name}',
                    need_login=True).json()['success']

    def add_to_music_playlist(self,music_playlist:MusicPlaylist,song:Song) -> bool:
        """
        Add a song to your music playlist

        Parameters
        ----------
            song: An object of Song type
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns false if song had been added already

        """
        songs = music_playlist.songs
        for sng in songs:
            if song.id == sng.id:
                return False

        return self.private_request('mp3_playlist_add',
                    params=f'id={music_playlist.id}&mp3={song.id}&start=0',
                    need_login=True).json()['success']

    def remove_from_music_playlist(self,music_playlist:MusicPlaylist,song:Song) -> bool:
        """
        Remove a song from your music playlist

        Parameters
        ----------
            song: An object of Song type
            music_playlist: An object of MusicPlaylist type

        Returns
        -------
            bool: returns false if song hadn't been added before

        """
        songs = music_playlist.songs
        for sng in songs:
            if song.id == sng.id:
                return self.private_request('mp3_playlist_item_remove',
                        params=f'type=mp3&id={music_playlist.id}&item={sng.item}',
                        need_login=True).json()['success']
        return False

class VideoPlayListMixin(PrivateRequest):
    def get_video_playlist_by_url(self,url:HttpUrl) -> VideoPlaylist:
        """
        Get video playlist info by site url (e.g. radiojavan.com/playlists/playlist/video/...)

        Parameters
        ----------
            url: Site url of video playlist

        Returns
        -------
            VideoPlaylist: An object of Video Playlist type

        """
        return self.get_video_playlist_by_id(url_to_id(url))

    def get_video_playlist_by_id(self,id:str) -> VideoPlaylist:
        """
        Get video playlist info by id

        Parameters
        ----------
            id: Unique id of video playlist

        Returns
        -------
            VideoPlaylist: An object of Video Playlist type

        """
        response = self.private_request('video_playlist_with_items',
                                params=f'id={id}').json()
        return extract_video_playlist(response) 

    def create_video_playlist(self,name:str,video:Video) -> Optional[str]:
        """
        Create a video playlist
        Note: in RJ you can't create empty playlist , so you need a video for creation playlist

        Parameters
        ----------
            name: Name of playlist
            video: An object of Video type

        Returns
        -------
            str: playlist's id

        """
        response = self.private_request('video_playlist_add',
                        params=f'type=video&video={video.id}&name={name}',
                        need_login=True).json()
        return response['playlist'] if response['success'] else None

    def delete_video_playlist(self,video_playlist:VideoPlaylist) -> bool:
        """
        Delete your video playlist

        Parameters
        ----------
            video_playlist: An object of VideoPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        return self.private_request('video_playlist_remove',
                        params=f'type=video&id={video_playlist.id}',
                        need_login=True).json()['success']

    def rename_video_playlist(self,video_playlist:VideoPlaylist,new_name:str) -> bool:
        """
        Rename your video playlist

        Parameters
        ----------
            new_name: The name you want to set for a playlist
            video_playlist: An object of VideoPlaylist type

        Returns
        -------
            bool: returns true if success

        """
        return self.private_request('video_playlist_rename',
                        params=f'type=video&id={video_playlist.id}&name={new_name}',
                        need_login=True).json()['success']

    def add_to_video_playlist(self,video_playlist:VideoPlaylist,video:Video) -> bool:
        """
        Add a video to your video playlist

        Parameters
        ----------
            video: An object of Video type
            video_playlist: An object of VideoPlaylist type

        Returns
        -------
            bool: returns false if video had been added already

        """
        videos = video_playlist.videos
        for vid in videos:
            if vid.id == video.id:
                return False
        return self.private_request('video_playlist_add',
                    params=f'type=video&video={video.id}&id={video_playlist.id}',
                    need_login=True).json()['success']
        
    def remove_from_video_playlist(self,video_playlist:VideoPlaylist,video:Video) -> bool:
        """
        Remove a video from your video playlist

        Parameters
        ----------
            video: An object of Video type
            video_playlist: An object of VideoPlaylist type

        Returns
        -------
            bool: returns false if video hadn't been added before

        """
        videos = video_playlist.videos
        for vid in videos:
            if vid.id == video.id:
                return self.private_request('video_playlist_item_remove',
                        params=f'type=video&id={video_playlist.id}&item={vid.item}',
                        need_login=True).json()['success']
        return False
        

    