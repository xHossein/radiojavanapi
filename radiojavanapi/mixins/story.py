from radiojavanapi.helper import url_to_id
from typing import Optional
from pydantic import HttpUrl
from radiojavanapi.extractors import extract_story
from radiojavanapi.mixins.private import PrivateRequest
from ..types import Story

class StoryMixin(PrivateRequest):
    LIKE_ENDPOINT = 'selfie_vote'
    TYPE = 'selfie'

    def get_story_by_url(self,url:HttpUrl) -> Optional[Story]:
        """
        Get story info by site url (e.g. radiojavan.com/story/...)

        Parameters
        ----------
            url: Site url of story (selfie)

        Returns
        -------
            Story: An object of Story type

        """
        return self.get_story_by_hash_id(url_to_id(url))

    def get_story_by_hash_id(self,hash_id:str) -> Optional[Story]:
        """
        Get story info by hash id

        Parameters
        ----------
            hash_id: Unique hash id of story (selfie)

        Returns
        -------
            Story: An object of Story type

        """
        response = self.private_request('selfie',
                    params=f'id={hash_id}').json()
        return extract_story(response) if response else None

    def like_story(self, story:Story) -> bool:
        """
        Like a story (selfie)

        Parameters
        ----------
            story: An object of Story type

        Returns
        -------
            bool: returns false if story had been liked already

        """
        return StoryMixin.__like__(self,story.id)

    def unlike_story(self, story:Story) -> bool:
        """
        UnLike a story (selfie)

        Parameters
        ----------
            story: An object of Story type

        Returns
        -------
            bool: returns false if story hadn't been liked before

        """
        return StoryMixin.__unlike__(self,story.id)
    

