from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_artist
from radiojavanapi.models import Artist
from radiojavanapi.helper import url_to_id

from pydantic import HttpUrl
from urllib.parse import quote_plus

class ArtistMixin(PrivateRequest):
    def get_artist_by_url(self, url: HttpUrl) -> Artist:
        """
        Get artist info by site url (e.g. radiojavan.com/artist/...)

        Arguments
        ----------
            url: Site url of artist

        Returns
        -------
            Artist: An object of Artist type

        """
        return self.get_artist_by_name(url_to_id(url))

    def get_artist_by_name(self, name: str) -> Artist:
        """
        Get artist info by name (must be the exact name on RadioJavan API)

        Arguments
        ----------
            name: Exact name of artist on RadioJavan API

        Returns
        -------
            Artist: Return An object of Artist type

        """
        response = self.private_request(
            'artist', params=f'query={quote_plus(name)}').json()
        return extract_artist(response)

    def follow_artist(self, name: str) -> bool:
        """
        Follow an artist

        Arguments
        ----------
            name: Exact name of artist on RadioJavan API

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('artist_follow',
                    params=f'artist={quote_plus(name)}',
                    need_login=True).json()
        return response['success'] == True

    def unfollow_artist(self, name: str) -> bool:
        """
        UnFollow an artist

        Arguments
        ----------
            name: Exact name of artist on RadioJavan API

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('artist_unfollow', 
                    params=f'artist={quote_plus(name)}',
                    need_login=True).json()
        return response['success'] == True
