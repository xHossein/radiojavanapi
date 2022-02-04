from radiojavanapi.helper import extract_cookie
from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.constants import BASE_HEADERS

class AuthMixin(PrivateRequest):
    def __init__(self) -> None:
        super().__init__()
        self.cookie = None

    def initial(self):
        """
        Initialize Login/SignUp helpers
        
        """
        if self.authorized:
            self.logout()
        
        self.private.cookies.clear()
        self.private.headers.update(BASE_HEADERS)
        self.cookie = None
        self.authorized = False
        self.email = None
        self.password = None
        self.update_cookie(self.private_request('app_config'))
    
    def update_cookie(self, response):
        """
        Extract cookie and update headers
        
        """
        self.cookie = extract_cookie(response.headers.get('Set-Cookie')) 
        self.private.headers.update({'Cookie': self.cookie})
        
    def login(self, email: str, password: str) -> bool:
        """
        Log in to RadioJavan

        Arguments
        ----------
            email: Your account email
            password: Your account password

        Returns
        -------
            bool: login result

        """
        self.initial()
        self.email = email
        self.password = password
        
        payload = { 
                "login_email": email,
                "login_password": password
        }
        
        response = self.private_request('login', json=payload)
        response_json = response.json()

        if response_json.get('success'):
            self.update_cookie(response)
            self.authorized = True
            
        return self.authorized
    
    def logout(self) -> bool:
        return self.private_request('logout', need_login=True).json()["success"]
    
    def signup(self,
               firstname: str, lastname: str,
               username: str, email: str, password: str,
               auto_login: bool = False) -> bool:
        
        """
        Sign up to RadioJavan

        Arguments
        ----------
            firstname: Your account firstname
            lastname: Your account lastname
            username: Your account username
            email: Your account email
            password: Your account password
            auto_login [optional]: login to account after sign up
            
        Returns
        -------
            bool: sign up result

        """
        self.initial()
        
        payload = {
            "email": email,
            "password": password,
            "username": username,
            "email_confirm": email,
            "firstname": firstname,
            "lastname": lastname
        }
        
        is_success = self.private_request('signup_mobile', json=payload).json()['success']   
        if is_success and auto_login:
            self.login(email, password)

        return is_success