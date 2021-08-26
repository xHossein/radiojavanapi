from radiojavanapi.mixins.user import UserMixin
from radiojavanapi.mixins.auth import AuthMixin
from radiojavanapi.models import Account, MyPlaylists, ShortUser
from radiojavanapi.extractors import extract_account, extract_my_playlists

from typing import List

class AccountMixin(AuthMixin, UserMixin):
    def account_info(self) -> Account:
        """
        Get private info for your account

        Returns
        -------
            Account: An object of Account type

        """
        response = self.private_request('user_profile', need_login=True).json()
        return extract_account(response)
    

    def account_edit(self,
                     firstname: str = None,
                     lastname: str = None,
                     username: str = None,
                     email: str = None,
                     bio: str = None,
                    _remove_photo: bool = False
                    ) -> Account:
        
        """
        Change profile data (e.g. email, firstname, ...).
        Note: To remove bio, pass empty string.

        Arguments
        ----------
            firstname: Account's firstname
            lastname : Account's lastname
            username : Account's username
            email    : Account's email
            
        Returns
        -------
            Account: An object of Account type

        """
        account = self.account_info()
        payload = {
            'firstname'  : firstname or account.firstname,
            'lastname'   : lastname  or account.lastname,
            'email'      : email     or account.email,
            'username'   : username  or account.username,
        }
        if _remove_photo:
            payload.update({"remove_photo": True})
            
        if bio != None:
            payload.update({"bio": bio})

        self.private_request('user_profile_update',
                             json=payload, need_login=True)
        return self.account_info()

    def change_password(self, password: str) -> bool:
        """
        Change your account password

        Arguments
        ----------
        password: Your new password

        Returns
        -------
            bool: Returns true if success

        """
        response = self.private_request('user_password_update',
                        json={
                            "oldpass" : self.password,
                            "newpass1": password,
                            "newpass2": password
                        }, need_login=True)
        
        response_json = response.json()
        if response_json['success']:
            self.password = password
            self.cookie = {
                            'Cookie': '_rj_web={}'.format(
                              response.headers['Set-Cookie'].split('_rj_web=')[1].split(';')[0]
                              )
                          }
            self.private.headers.update(self.cookie)
            return True
        return False

    def upload_photo(self, photo_path: str) -> bool:
        """
        Upload your profile photo (support jpg/png)

        Arguments
        ----------
        photo_path:
            Path to the image you want to upload

        Returns
        -------
            bool: Returns true if success

        """
        account = self.account_info()
        with open(photo_path, 'rb') as photo:
            fields = {
                'firstname': account.firstname,
                'lastname': account.lastname,
                'email': account.email,
                'username': account.username,
                'remove_photo': 'undefined',
                'photo': ('0', photo, 'image/jpeg')
            }
            return self.private_request('user_profile_update',
                        fields=fields , need_login=True).json()['success']

    def remove_photo(self) -> bool:
        """
        Remove your profile photo

        Returns
        -------
            bool: Returns true if removed successfully

        """
        account = self.account_edit(_remove_photo = True)
        return account.has_custom_photo != True

    def deactive_account(self) -> bool:
        """
        Deactivate your profile and logout

        Returns
        -------
            bool: Returns true if success

        """
        if self.private_request('deactivate',
                    need_login=True).json()['success'] and self.logout():
            return True
        return False

    def following_artists(self) -> List[str]:
        """
        Get list of artist names which you've followed

        Returns
        -------
            List: names list

        """
        return self.account_info().artists_name

    def my_followers(self) -> List[ShortUser]:
        """
        Get list of your followers

        Returns
        -------
            List[ShortUser]: list of your followers as ShortUser object

        """
        return self.get_user_followers(self.account_info().username)
    
    def my_following(self) -> List[ShortUser]:
        """
        Get list of user which you've followed

        Returns
        -------
            List[ShortUser]: list of your following as ShortUser object

        """
        return self.get_user_following(self.account_info().username)
    
    def my_playlists(self) -> MyPlaylists:
        """
        Get your MusicPlaylist & VideoPlaylist' shortdata as MyPlaylists Object

        Returns
        -------
            MyPlaylists: An object of MyPlaylists type
            
        """
        response = self.private_request('playlists_dash', need_login=True).json()  
        return extract_my_playlists(response)
  