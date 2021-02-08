from pydantic import HttpUrl
from radiojavanapi.extractors import extract_podcast
from radiojavanapi.mixins.private import PrivateRequest
from ..types import Podcast
from ..helper import url_to_id

class PodcastMixin(PrivateRequest):
    LIKE_ENDPOINT = 'podcast_vote'
    TYPE = 'podcast'

    def get_podcast_by_url(self,url:HttpUrl) -> Podcast:
        """
        Get podcast info by site url (e.g. radiojavan.com/podcasts/podcast/...)

        Parameters
        ----------
            url: Site url of podcast

        Returns
        -------
            Podcast: An object of Podcast type

        """
        return self.get_podcast_by_id(url_to_id(url))

    def get_podcast_by_id(self,id:int) -> Podcast:
        """
        Get podcast info by id

        Parameters
        ----------
            id: Unique id of podcast

        Returns
        -------
            Podcast: An object of Podcast type

        """
        response = self.private_request('podcast',
                        params=f'id={id}').json()
        return extract_podcast(response)

    def like_podcast(self,podcast:Podcast) -> bool:
        """
        Like a podcast

        Parameters
        ----------
            podcast: An object of Podcast type

        Returns
        -------
            bool: returns false if podcast had been liked already

        """
        return PodcastMixin.__like__(self,podcast.id)

    def unlike_podcast(self,podcast:Podcast) -> bool:
        """
        UnLike a podcast

        Parameters
        ----------
            podcast: An object of Podcast type

        Returns
        -------
            bool: returns false if podcast hadn't been liked before

        """
        return PodcastMixin.__unlike__(self,podcast.id)

