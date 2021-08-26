from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.extractors import  extract_short_user, extract_user
from radiojavanapi.models import ShortUser, User
from radiojavanapi.helper import url_to_id

from pydantic import HttpUrl
from typing import List

class UserMixin(PrivateRequest):
    def get_user_by_url(self, url: HttpUrl) -> User:
        """
        Get user info by site url (e.g. radiojavan.com/u/...)

        Arguments
        ----------
            url: Site url of user

        Returns
        -------
            User: An object of User type

        """
        return self.get_user_by_username(url_to_id(url))

    def get_user_by_username(self, username: str) -> User:
        """
        Get user info by usename 
        
        Arguments
        ----------
            username: username of user

        Returns
        -------
            User: An object of User type

        """
        response = self.private_request(
            'user_profile', params=f'stats=1&username={username}').json()
        return extract_user(response)
    
    def get_user_followers(self, username: str) -> List[ShortUser]:
        """
        Get user followers list
        
        Arguments
        ----------
            username: username of user

        Returns
        -------
            List[ShortUser]: list of user followers as ShortUser object

        """
        response = self.private_request(
            'user_followers_list', params=f'username={username}').json()
        return [extract_short_user(user) for user in response]
    
    def get_user_following(self, username: str) -> List[ShortUser]:
        """
        Get user following list
        
        Arguments
        ----------
            username: username of user

        Returns
        -------
            List[ShortUser]: list of user following as ShortUser object

        """
        response = self.private_request(
            'user_following_list', params=f'username={username}').json()
        return [extract_short_user(user) for user in response]

    def follow_user(self, username: str) -> bool:
        """
        Follow a user

        Arguments
        ----------
            username: username of user

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('user_follow',
                    json={"username":username},
                    need_login=True).json()
        return response['success'] == True
    
    def unfollow_user(self, username: str) -> bool:
        """
        UnFollow a user

        Arguments
        ----------
            username: username of user

        Returns
        -------
            bool: RJ api result

        """
        response = self.private_request('user_unfollow',
                    json={"username":username},
                    need_login=True).json()
        return response['success'] == True
