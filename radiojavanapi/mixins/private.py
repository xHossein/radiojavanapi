from radiojavanapi.constants import API_DOMAIN, BASE_HEADERS
from radiojavanapi.exceptions import (
                BadCredentials, ClientJSONDecodeError, ClientConnectionError, DuplicatePassword,
                EmailExists, ClientLoginRequired, LongString, InvalidName, DuplicateName,
                UnknownError, UsernameExists, ClientLoginRequired, InvalidMediaId
                )

import requests
from json.decoder import JSONDecodeError
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PrivateRequest():
    def __init__(self) -> None:
        self.private = requests.Session()
        self.private.headers = BASE_HEADERS
        self.authorized = False
        self.email = None
        self.password = None

    def private_request(self,endpoint,data=None,json=None,fields=None,
                            params=None,headers=None,need_login=False):
        if need_login and not self.authorized:
            raise ClientLoginRequired("to use this method, you need to login first.")

        if headers:
            self.private.headers.update(headers)

        response = None
        try:
            if data:
                response = self.private.post(API_DOMAIN.format(endpoint), data=data, params=params)
            elif json:
                response = self.private.post(API_DOMAIN.format(endpoint), json=json, params=params)
            elif fields:
                multipart_data = MultipartEncoder(fields=fields)
                response = self.private.post(API_DOMAIN.format(endpoint), data=multipart_data,
                                            headers={
                                                    **{'Content-Type': multipart_data.content_type},
                                                    **self.private.headers
                                                    }
                                            )
            else:
                response = self.private.get(API_DOMAIN.format(endpoint), params=params)
                
        except requests.exceptions.RequestException:
            raise ClientConnectionError()
        
        except Exception as e: # TO DO
            raise UnknownError(e)
        
        response_json = None
        try:
            response_json = response.json()
        except JSONDecodeError as e:
            raise ClientJSONDecodeError(f"JSONDecodeError {e} while opening {response.url}")

        if isinstance(response_json, dict) and response_json.get('success') == False and 'user_subscription' not in response.url:
            msg = response_json.get('msg')
            if msg:
                if 'is too long' in msg:
                    raise LongString(msg)
                elif 'Invalid email' in msg:
                    raise BadCredentials(msg)
                elif 'only contain letters' in msg:
                    raise InvalidName(msg)
                elif 'already have that email' in msg:
                    raise EmailExists(msg)
                elif 'username is not available' in msg:
                    raise UsernameExists(msg)
                elif 'Name already exists.' == msg:
                    raise DuplicateName('Playlist with this name already exists.')
                elif 'Playlist with this name already exists.' == msg:
                    raise DuplicateName(msg)
                elif 'new password cannot be the same' in msg:
                    raise DuplicatePassword(msg)
                else: # TO DO
                    raise UnknownError(msg)
                
            elif len(response_json) == 1:
                raise InvalidMediaId(f"An invalid media is was provided.")
            else:
                raise UnknownError(response_json)

        return response

    #### these are for like song/video/podcast/story:
    @classmethod
    def __like__(cls, self, id):
        if 'vote' in cls.__toggle_like__(self, id):
            return True
        else:
            cls.__toggle_like__(self, id)
            return False

    @classmethod
    def __unlike__(cls, self, id):
        if 'vote' in cls.__toggle_like__(self, id):
            cls.__toggle_like__(self, id)
            return False
        else:
            return True

    @classmethod
    def __toggle_like__(cls, self, id):
        return self.private_request(cls.LIKE_ENDPOINT,
                params=f'id={id}&type={cls.TYPE}&vote=5&remove=1',
                need_login=True).json()