from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import extract_video
from radiojavanapi.models import Video
from radiojavanapi.helper import url_to_id

from typing import List, Union
from pydantic import HttpUrl

class VideoMixin(PrivateRequest):
    LIKE_ENDPOINT = 'video_vote'
    TYPE = 'video'

    def get_video_by_url(self, url: HttpUrl) -> Video:
        """
        Get video info by site url (e.g. radiojavan.com/videos/video/...)

        Arguments
        ----------
            url: Site url of video

        Returns
        -------
            Video: An object of Video type

        """
        return self.get_video_by_id(url_to_id(url))

    def get_video_by_id(self, id: Union[int, str]) -> Video:
        """
        Get video info by id

        Arguments
        ----------
            id: Unique id of video

        Returns
        -------
            Video: An object of Video type

        """
        response =  self.private_request('video',
                    params=f'id={id}').json()
        return extract_video(response)

    def like_video(self, video_id: Union[int, str]) -> bool:
        """
        Like a video

        Arguments
        ----------
            video_id: A digit id of Video

        Returns
        -------
            bool: Returns false if video had been liked already

        """
        return VideoMixin.__like__(self, video_id)

    def unlike_video(self, video_id: Union[int, str]) -> bool:
        """
        UnLike a video

        Arguments
        ----------
            video_id: A digit id of Video

        Returns
        -------
            bool: Returns false if video hadn't been liked before

        """
        return VideoMixin.__unlike__(self, video_id)

    def liked_videos(self) -> List[Video]:
        """
        Get list of videos you had liked

        Returns
        -------
            List: A list of Video object

        """
        response = self.private_request(
                    'videos_liked', need_login=True).json()
        return [extract_video(video) for video in response]