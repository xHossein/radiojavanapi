from radiojavanapi.mixins.private import PrivateRequest

class Auth(PrivateRequest):
    def __init__(self) -> None:
        super().__init__()
        self.cookie = None

    def login(self, email: str, password: str) -> bool:
        """
        Log in to RadioJavan

        Parameters
        ----------
            email: Your account's email
            password: Your account's password

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