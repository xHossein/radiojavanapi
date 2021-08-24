from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.constants import BASE_HEADERS

class AuthMixin(PrivateRequest):
    def __init__(self) -> None:
        super().__init__()
        self.cookie = None

    def login(self, email: str, password: str) -> bool:
        """
        Log in to RadioJavan

        Arguments
        ----------
            email: Your account email
            password: Your account password

        Returns
        -------
            bool: auth status

        """
        self.email = email
        self.password = password
        response = self.private_request(
            'login', json={"login_email": f"{email}", "login_password": f"{password}"})
        response_json = response.json()

        if response_json.get('success'):
            self.cookie = {
                            'Cookie': '__cfduid={}; _rj_web={}'.format(
                              response.cookies.get('__cfduid'),
                              response.cookies.get('_rj_web',)
                              )
                          }
            self.private.headers.update(self.cookie)
            self.authorized = True
        return self.authorized
    
    def logout(self) -> bool:
        response = self.private_request('logout',
                                need_login=True).json()["success"]
        if response:
            self.cookie = None
            self.authorized = False
            self.email = None
            self.password = None
            self.private.cookies.clear()
            self.private.headers.clear()
            self.private.headers.update(BASE_HEADERS)
            return True
        return False