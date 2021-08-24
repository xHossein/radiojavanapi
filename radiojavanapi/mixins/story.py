from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_story
from radiojavanapi.models import Story
from radiojavanapi.helper import url_to_id

from typing import Union
from pydantic import HttpUrl

class StoryMixin(PrivateRequest):
    LIKE_ENDPOINT = 'selfie_vote'
    TYPE = 'selfie'

    def get_story_by_url(self, url: HttpUrl) -> Story:
        """
        Get story info by site url (e.g. radiojavan.com/story/...)

        Arguments
        ----------
            url: Site url of story (selfie)

        Returns
        -------
            Story: An object of Story type

        """
        return self.get_story_by_hash_id(url_to_id(url))

    def get_story_by_hash_id(self, hash_id: str) -> Story:
        """
        Get story info by hash id

        Arguments
        ----------
            hash_id: Unique hash id of story (selfie)

        Returns
        -------
            Story: An object of Story type

        """
        response = self.private_request('selfie',
                    params=f'id={hash_id}').json()
        return extract_story(response)

    def like_story(self, story_id: Union[int, str]) -> bool:
        """
        Like a story (selfie)

        Arguments
        ----------
            story_id: A digit id of stroy

        Returns
        -------
            bool: Returns false if story had been liked already

        """
        return StoryMixin.__like__(self, story_id)

    def unlike_story(self, story_id: Union[int, str]) -> bool:
        """
        UnLike a story (selfie)

        Arguments
        ----------
            story_id: A digit id of stroy

        Returns
        -------
            bool: Returns false if story hadn't been liked before

        """
        return StoryMixin.__unlike__(self, story_id)
    

