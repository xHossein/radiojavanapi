from typing import Optional
from pydantic import HttpUrl
from radiojavanapi.extractors import extract_artist
from radiojavanapi.mixins.private import PrivateRequest
from ..types import Artist
from ..helper import url_to_id


class ArtistMixin(PrivateRequest):
    def get_artist_by_url(self, url: HttpUrl) -> Artist:
        """
        Get artist info by site url (e.g. radiojavan.com/artist/...)

        Parameters
        ----------
            url: Site url of artist

        Returns
        -------
            Artist: An object of Artist type

        """
        return self.get_artist_by_name(url_to_id(url))

    def get_artist_by_name(self, name: str) -> Optional[Artist]:
        """
        Get artist info by name (must be the exact name on RadioJavan)

        Parameters
        ----------
            name: Exact name of artist on RadioJavan

        Returns
        -------
            Artist: Return An object of Artist type

        """
        response = self.private_request(
            'artist', params=f'query={name}').json()
        return extract_artist(response)

    def follow_artist(self, artist: Artist) -> bool:
        """
        Follow an artist

        Parameters
        ----------
            artist: An object of Artist type

        Returns
        -------
            bool: returns false if artist had been followed already

        """
        response = self.private_request('artist_follow',
                    params='artist={}'.format(artist.name.replace(' ', '+')),
                    need_login=True).json()
        return True if response['success'] else False

    def unfollow_artist(self, artist: Artist) -> bool:
        """
        UnFollow an artist

        Parameters
        ----------
            artist: An object of Artist type

        Returns
        -------
            bool: returns false if artist hadn't been followed before

        """
        response = self.private_request('artist_unfollow', 
                    params='artist={}'.format(artist.name.replace(' ', '+')),
                    need_login=True).json()
        return True if response['success'] else False
