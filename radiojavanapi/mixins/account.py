
from typing import Dict, List
from ..types import Account
from radiojavanapi.extractors import extract_account
from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.constants import BASE_HEADERS

class AccountMixin(PrivateRequest):
    def account_info(self) -> Account:
        """
        Get private info for your account

        Returns
        -------
            Account: An object of Account type

        """
        response = self.private_request('user_profile',
                                        params='stats=1',
                                        need_login=True).json()
        response['has_subscription'] = self.private_request('user_subscription',
                                            need_login=True).json()['success']
        return extract_account(response)
    

    def account_edit(self, data:dict) -> Account:
        """
        Change profile data (e.g. email, firstname, lastname, username)

        Parameters
        ----------
            data: Fields you want to edit in your account as key and value pairs

        Returns
        -------
            Account: An object of Account type

        """
        account = self.account_info().dict()
        fields = ['firstname', 'lastname', 'email', 'username','remove_photo']
        updated_data = {key: account[key] 
                for key in fields if key in account}  
        updated_data.update({k:v for k,v in data.items() if k in fields})
        self.private_request('user_profile_update',
                             json=updated_data,need_login=True)
        return self.account_info()

    def change_password(self,password:str) -> bool:
        """
        Change your account's password

        Parameters
        ----------
        password: Your new password

        Returns
        -------
            bool: returns true if success

        """
        response = self.private_request('user_password_update',
                        json={
                            "oldpass":self.password,
                            "newpass1":password,
                            "newpass2":password
                        },need_login=True).json()['success']
        if response:
            self.password = password
            return True
        return False

    def change_photo(self,photo_path:str) -> bool:
        """
        Change photo for your profile (support jpg/png)

        Parameters
        ----------
        photo_path:
            Path to the image you want to update as your profile photo

        Returns
        -------
            bool: returns true if success

        """
        account = self.account_info()
        fields = {'firstname': account.firstname,
                 'lastname': account.lastname,
                 'email': account.email,
                 'username': account.username,
                 'remove_photo': 'undefined',
                 'photo': ('0', open(photo_path, 'rb'), 'image/jpeg')}
        return self.private_request('user_profile_update',
                    fields=fields , need_login=True).json()['success']

    def remove_photo(self) -> Account:
        """
        Remove photo for your profile

        Returns
        -------
            Account: An object of Account type

        """
        return self.account_edit(remove_photo=True)

    def deactive_account(self) -> bool:
        """
        Deactivate your profile and logout

        Returns
        -------
            bool: returns true if success

        """
        if self.private_request('deactivate',need_login=True).json()['success']:
            self.private_request('logout',need_login=True)
            self.private.headers = BASE_HEADERS
            self.authorized = False
            return True
        return False

    def my_following(self) -> List[str]:
        """
        Get list of artists name which you follow

        Returns
        -------
            List: names list

        """
        return self.account_info().artists_name

    def my_playlists(self) -> Dict:
        """
        Get your MusicPlaylist & VideoPlaylist's id and title as Dict

        Returns
        -------
            Dict: Playlists id and title as Dict

        """
        response = self.private_request('playlists_dash',need_login=True).json()  
        return {
                "music_playlists": [{k: mpl[k] for k in ('id', 'title')}
                                    for mpl in response['mp3s']['myplaylists']],
                "video_playlists": [{k: vpl[k] for k in ('id', 'title')}
                                    for vpl in response['videos']['myplaylists']]
                }
  