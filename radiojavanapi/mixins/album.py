from radiojavanapi.mixins.search import SearchMixin
from typing import List, Optional
from pydantic import HttpUrl
from radiojavanapi.extractors import extract_album
from ..types import Album
from ..helper import url_to_id


class AlbumMixin(SearchMixin):
    def get_album_by_url(self,url:HttpUrl) -> Optional[Album]:
        """
        Get album info by site url (e.g. radiojavan.com/mp3s/album/...)

        Parameters
        ----------
            url: Site url of album

        Returns
        -------
            Album: An object of Album type

        """
        query = url_to_id(url).lower().replace('-',' ')
        albums_id = self.search(query).albums_id
        for id in albums_id:
            album = self.private_request('mp3',
                    params=f'id={id}').json()
            if album.get('album_album').lower() in query and \
                album.get('album_artist').lower() in query:
                return extract_album(album)

    def get_album_by_id(self,id:int) -> Optional[Album]:
        """
        Get album info by id

        Parameters
        ----------
            id: this id belong to one of album-tracks

        Returns
        -------
            Album: An object of Album type

        """
        album = self.private_request('mp3',
                params=f'id={id}').json()
        return extract_album(album)

