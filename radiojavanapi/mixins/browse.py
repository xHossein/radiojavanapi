from radiojavanapi.mixins.album import AlbumMixin
from radiojavanapi.types import (Album, Artist, ComingSoon,
                                Podcast, Song, Story, Video)
from radiojavanapi.extractors import (extract_song, extract_podcast, extract_story,
                                    extract_video, extract_coming_soon)
from radiojavanapi.mixins.artist import ArtistMixin
from typing import List

class BrowseMixin(ArtistMixin,AlbumMixin):
    def __browse_req__(self,endpoint,type):
        extractor = None
        if type == 'albums':
            extractor = self.get_album_by_id
        elif endpoint == "mp3s":
            extractor = extract_song
        elif endpoint == "videos":
            extractor = extract_video
        elif endpoint == "podcasts":
            extractor = extract_podcast

        page, items, response = 1, [], {""}
        while bool(response):
            response = self.private_request(endpoint,
                        params=f'url={endpoint}&type={type}&page={page}').json()
            items.extend([extractor(item['id'] if type=='albums' else item) for item in response])
            page+=1
        return items

    def get_latest_stories(self) -> List[Story]:
        """Get list of latest stories"""
        response = self.private_request('selfies_browse',
                        params='url=selfies_browse').json()
        return [extract_story(story) for story in response] 
    
    def get_trending_songs(self) -> List[Song]:
        """Get list of trending songs"""
        return self.__browse_req__('mp3s','trending')
    
    def get_popular_songs(self) -> List[Song]:
        """Get list of popular songs"""
        return self.__browse_req__('mp3s','popular')

    def get_featured_songs(self) -> List[Song]:
        """Get list of featured songs"""
        return self.__browse_req__('mp3s','featured')
    
    def get_latest_albums(self) -> List[Album]:
        """Get list of latest albums"""
        return self.__browse_req__('mp3s','albums')

    def get_trending_videos(self) -> List[Video]:
        """Get list of trending videos"""
        return self.__browse_req__('videos','trending')

    def get_popular_videos(self) -> List[Video]:
        """Get list of popular videos"""
        return self.__browse_req__('videos','popular')

    def get_featured_videos(self) -> List[Video]:
        """Get list of featured videos"""
        return self.__browse_req__('videos','featured')

    def get_latest_videos(self) -> List[Video]:
        """Get list of latest videos"""
        return self.__browse_req__('videos','latest')

    def get_popular_podcasts(self) -> List[Podcast]:
        """Get list of popular podcasts"""
        return self.__browse_req__('podcasts','popular')

    def get_featured_podcasts(self) -> List[Podcast]:
        """Get list of featured podcasts"""
        return self.__browse_req__('podcasts','featured')

    def get_talk_podcasts(self) -> List[Podcast]:
        """Get list of talk podcasts"""
        return self.__browse_req__('podcasts','talk')

    def get_shows_podcasts(self) -> List[Podcast]:
        """Get list of shows podcasts"""
        return self.__browse_req__('podcasts','shows')

    def get_coming_soon(self) -> List[ComingSoon]:
        """Get list of comingsoon songs/videos"""
        response = self.private_request('browse_items',params='v=2')
        items = response.json()['sections'][14]['items']
        return [extract_coming_soon(comingsoon) for comingsoon in items]

    def get_popular_artists(self) -> List[Artist]:
        """Get list of popular artists"""
        response = self.private_request('browse_items',params='v=2')
        items = response.json()['sections'][16]['items']
        return [self.get_artist_by_name(artist['name']) for artist in items]