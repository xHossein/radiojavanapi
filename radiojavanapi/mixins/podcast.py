from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_podcast
from radiojavanapi.models import Podcast
from radiojavanapi.helper import url_to_id

from typing import Union
from pydantic import HttpUrl

class PodcastMixin(PrivateRequest):
    LIKE_ENDPOINT = 'podcast_vote'
    TYPE = 'podcast'

    def get_podcast_by_url(self, url: HttpUrl) -> Podcast:
        """
        Get podcast info by site url (e.g. radiojavan.com/podcasts/podcast/...)

        Arguments
        ----------
            url: Site url of podcast

        Returns
        -------
            Podcast: An object of Podcast type

        """
        return self.get_podcast_by_id(url_to_id(url))

    def get_podcast_by_id(self, id: Union[int, str]) -> Podcast:
        """
        Get podcast info by id

        Arguments
        ----------
            id: Unique id of podcast

        Returns
        -------
            Podcast: An object of Podcast type

        """
        response = self.private_request('podcast',
                        params=f'id={id}').json()
        return extract_podcast(response)

    def like_podcast(self, podcast_id: Union[int, str]) -> bool:
        """
        Like a podcast

        Arguments
        ----------
            podcast_id: A digit id of podcast

        Returns
        -------
            bool: Returns false if podcast had been liked already

        """
        return PodcastMixin.__like__(self, podcast_id)

    def unlike_podcast(self, podcast_id: Union[int, str]) -> bool:
        """
        UnLike a podcast

        Arguments
        ----------
            podcast_id: A digit id of podcast

        Returns
        -------
            bool: Returns false if podcast hadn't been liked before

        """
        return PodcastMixin.__unlike__(self, podcast_id)

