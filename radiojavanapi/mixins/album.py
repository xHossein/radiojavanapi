from radiojavanapi.mixins.search import SearchMixin
from radiojavanapi.extractors import extract_album
from radiojavanapi.models import Album
from radiojavanapi.helper import url_to_id

from typing import Union
from pydantic import HttpUrl

class AlbumMixin(SearchMixin):
    def get_album_by_url(self, url: HttpUrl) -> Album:
        """
        Get album info by site url (e.g. radiojavan.com/mp3s/album/...)

        Arguments
        ----------
            url: Site url of album

        Returns
        -------
            Album: An object of Album type

        """
        query = url_to_id(url).lower().replace('-',' ')
        albums = self.search(query).albums
        for album in albums:
            if album.artist.lower() in query and album.name.lower() in query:
                return self.get_album_by_id(album.id)

    def get_album_by_id(self, id: Union[int, str]) -> Album:
        """
        Get album info by id

        Arguments
        ----------
            id: This id belong to one of album-tracks

        Returns
        -------
            Album: An object of Album type

        """
        album = self.private_request('mp3',
                params=f'id={id}').json()
        return extract_album(album)

