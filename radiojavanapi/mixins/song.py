from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_song
from radiojavanapi.models import Song
from radiojavanapi.helper import url_to_id

from typing import List, Union
from pydantic import HttpUrl

class SongMixin(PrivateRequest):
    LIKE_ENDPOINT = 'mp3_vote'
    TYPE = 'mp3'

    def get_song_by_url(self, url: HttpUrl) -> Song:
        """
        Get song info by site url (e.g. radiojavan.com/mp3s/mp3/...)

        Arguments
        ----------
            url: Site url of song (mp3)

        Returns
        -------
            Song: An object of Song type

        """
        return self.get_song_by_id(url_to_id(url))

    def get_song_by_id(self, id: Union[int, str]) -> Song:
        """
        Get song info by id

        Arguments
        ----------
            id: A digit id of Song (mp3)

        Returns
        -------
            Song: An object of Song type

        """
        response = self.private_request('mp3',
                    params=f'id={id}').json()
        return extract_song(response)

    def like_song(self, song_id: Union[int, str]) -> bool:
        """
        Like a song

        Arguments
        ----------
            song: A digit id of Song

        Returns
        -------
            bool: Returns false if song had been liked already

        """
        return SongMixin.__like__(self, song_id)

    def unlike_song(self, song_id: Union[int, str]) -> bool:
        """
        UnLike a song

        Arguments
        ----------
            song: A digit id of Song

        Returns
        -------
            bool: Returns false if song hadn't been liked before

        """
        return SongMixin.__unlike__(self, song_id)

    def liked_songs(self) -> List[Song]:
        """
        Get list of songs you had liked

        Returns
        -------
            List: A list of Song object

        """
        response = self.private_request('mp3s_liked', need_login=True).json()
        return [extract_song(song) for song in response]