from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_video_playlist, extract_music_playlist
from radiojavanapi.helper import url_to_id
from radiojavanapi.models import MusicPlaylist, VideoPlaylist

from typing import Optional, Union
from pydantic import HttpUrl

class MusicPlayListMixin(PrivateRequest):
    def get_music_playlist_by_url(self, url: HttpUrl) -> MusicPlaylist:
        """
        Get music playlist info by site url (e.g. radiojavan.com/playlists/playlist/mp3/...)

        Arguments
        ----------
            url: Site url of music playlist

        Returns
        -------
            MusicPlaylist: An object of Music Playlist type

        """
        return self.get_music_playlist_by_id(url_to_id(url))

    def get_music_playlist_by_id(self, id: str) -> MusicPlaylist:
        """
        Get music playlist info by id

        Arguments
        ----------
            id: Unique id of music playlist

        Returns
        -------
            MusicPlaylist: An object of Music Playlist type

        """
        response = self.private_request('mp3_playlist_with_items',
                                        params=f'id={id}').json()
        return extract_music_playlist(response)

    def follow_music_playlist(self, id: str) -> bool:
        """
        Follow a music playlist

        Arguments
        ----------
            id: An id of music playlist

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('mp3_playlist_follow',
                                params=f'id={id}&type=mp3',
                                need_login=True).json()
        return response['success'] == True

    def unfollow_music_playlist(self, id: str) -> bool:
        """
        UnFollow a music playlist

        Arguments
        ----------
            id: An id of music playlist

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('mp3_playlist_unfollow',
                                params=f'id={id}&type=mp3',
                                need_login=True).json()
        return response['success'] == True

    def create_music_playlist(self, name: str, song_id: Union[int, str]) -> Optional[str]:
        """
        Create a music playlist
        Note: in RJ you can't create empty playlist , so you need a song for creating playlist

        Arguments
        ----------
            name: Name of playlist
            song_id: A digit id of Song

        Returns
        -------
            str: Playlist's id

        """
        response = self.private_request('mp3_playlist_add',
                                params=f'type=mp3&mp3={song_id}&name={name}',
                                need_login=True).json()
        return response['playlist'] if response['success'] else None

    def delete_music_playlist(self, id: str) -> bool:
        """
        Delete your music playlist

        Arguments
        ----------
            id: An id of music playlist

        Returns
        -------
            bool: Returns true if success

        """
        return self.private_request('mp3_playlist_remove',
                        params=f'type=mp3&id={id}',
                        need_login=True).json()['success']

    def rename_music_playlist(self, id: str, name: str) -> bool:
        """
        Rename your music playlist

        Arguments
        ----------
            id: An id of music playlist
            name: The name you want to set for a playlist

        Returns
        -------
            bool: Returns true if success

        """
        return self.private_request('mp3_playlist_rename',
                    params=f'type=mp3&id={id}&name={name}',
                    need_login=True).json()['success']

    def add_to_music_playlist(self, id: str, song_id: Union[int, str]) -> bool:
        """
        Add a song to your music playlist

        Arguments
        ----------
            id: An id of music playlist
            song_id: A digit id of Song

        Returns
        -------
            bool: Returns false if song had been added already

        """
        songs = self.get_music_playlist_by_id(id).songs
        for sng in songs:
            if song_id == sng.id:
                return False

        return self.private_request('mp3_playlist_add',
                    params=f'id={id}&mp3={song_id}&start=0',
                    need_login=True).json()['success']

    def remove_from_music_playlist(self, id: str, song_id: Union[int, str]) -> bool:
        """
        Remove a song from your music playlist

        Arguments
        ----------
            id: An id of music playlist
            song_id: A digit id of Song

        Returns
        -------
            bool: Returns false if song hadn't been added before

        """
        songs = self.get_music_playlist_by_id(id).songs
        for sng in songs:
            if song_id == sng.id:
                return self.private_request('mp3_playlist_item_remove',
                        params=f'type=mp3&id={id}&item={sng.item}',
                        need_login=True).json()['success']
        return False

class VideoPlayListMixin(PrivateRequest):
    def get_video_playlist_by_url(self, url: HttpUrl) -> VideoPlaylist:
        """
        Get video playlist info by site url (e.g. radiojavan.com/playlists/playlist/video/...)

        Arguments
        ----------
            url: Site url of video playlist

        Returns
        -------
            VideoPlaylist: An object of Video Playlist type

        """
        return self.get_video_playlist_by_id(url_to_id(url))

    def get_video_playlist_by_id(self, id: str) -> VideoPlaylist:
        """
        Get video playlist info by id

        Arguments
        ----------
            id: Unique id of video playlist

        Returns
        -------
            VideoPlaylist: An object of Video Playlist type

        """
        response = self.private_request('video_playlist_with_items',
                                params=f'id={id}').json()
        return extract_video_playlist(response) 

    def create_video_playlist(self, name: str, video_id: Union[int, str]) -> Optional[str]:
        """
        Create a video playlist
        Note: in RJ you can't create empty playlist , so you need a video for creating playlist

        Arguments
        ----------
            name: Name of playlist
            video_id: A digit id of Video

        Returns
        -------
            str: Playlist's id

        """
        response = self.private_request('video_playlist_add',
                        params=f'type=video&video={video_id}&name={name}',
                        need_login=True).json()
        return response['playlist'] if response['success'] else None

    def delete_video_playlist(self, id: str) -> bool:
        """
        Delete your video playlist

        Arguments
        ----------
            id: An id of video playlist

        Returns
        -------
            bool: Returns true if success

        """
        return self.private_request('video_playlist_remove',
                        params=f'type=video&id={id}',
                        need_login=True).json()['success']

    def rename_video_playlist(self, id: str, name: str) -> bool:
        """
        Rename your video playlist

        Arguments
        ----------
            id: An id of video playlist
            name: The name you want to set for a playlist

        Returns
        -------
            bool: Returns true if success

        """
        return self.private_request('video_playlist_rename',
                        params=f'type=video&id={id}&name={name}',
                        need_login=True).json()['success']

    def add_to_video_playlist(self, id: str, video_id: Union[int, str]) -> bool:
        """
        Add a video to your video playlist

        Arguments
        ----------
            id: An id of video playlist
            video_id: A digit id of Video

        Returns
        -------
            bool: Returns false if video had been added already

        """
        videos = self.get_video_playlist_by_id(id).videos
        for vid in videos:
            if vid.id == video_id:
                return False
            
        return self.private_request('video_playlist_add',
                    params=f'type=video&video={video_id}&id={id}',
                    need_login=True).json()['success']
        
    def remove_from_video_playlist(self, id: str, video_id: Union[int, str]) -> bool:
        """
        Remove a video from your video playlist

        Arguments
        ----------
            id: An id of video playlist
            video_id: A digit id of Video

        Returns
        -------
            bool: Returns false if video hadn't been added before

        """
        videos = self.get_video_playlist_by_id(id).videos
        for vid in videos:
            if vid.id == video_id:
                return self.private_request('video_playlist_item_remove',
                        params=f'type=video&id={id}&item={vid.item}',
                        need_login=True).json()['success']
        return False
        

    