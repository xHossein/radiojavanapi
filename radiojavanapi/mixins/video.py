from typing import List
from pydantic import HttpUrl
from radiojavanapi.extractors import extract_video
from radiojavanapi.mixins.private import PrivateRequest
from ..types import Video
from ..helper import url_to_id

class VideoMixin(PrivateRequest):
    LIKE_ENDPOINT = 'video_vote'
    TYPE = 'video'

    def get_video_by_url(self,url:HttpUrl) -> Video:
        """
        Get video info by site url (e.g. radiojavan.com/videos/video/...)

        Parameters
        ----------
            url: Site url of video

        Returns
        -------
            Video: An object of Video type

        """
        return self.get_video_by_id(url_to_id(url))

    def get_video_by_id(self,id:int) -> Video:
        """
        Get video info by id

        Parameters
        ----------
            id: Unique id of video

        Returns
        -------
            Video: An object of Video type

        """
        response =  self.private_request('video',
                    params=f'id={id}').json()
        return extract_video(response)

    def like_video(self,video:Video) -> bool:
        """
        Like a video

        Parameters
        ----------
            video: An object of Video type

        Returns
        -------
            bool: returns false if video had been liked already

        """
        return VideoMixin.__like__(self,video.id)

    def unlike_video(self,video:Video) -> bool:
        """
        UnLike a video

        Parameters
        ----------
            video: An object of Video type

        Returns
        -------
            bool: returns false if video hadn't been liked before

        """
        return VideoMixin.__unlike__(self,video.id)

    def liked_videos(self) -> List[Video]:
        """
        Get list of videos you had liked

        Returns
        -------
            List: a list of Video object

        """
        response =  self.private_request('videos_liked',
                    need_login=True).json()
        return [extract_video(video) for video in response]