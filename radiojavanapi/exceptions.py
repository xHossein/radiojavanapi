class ClientError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ClientLoginRequired(ClientError):
    pass

class ClientJSONDecodeError(ClientError):
    pass

class ClientConnectionError(ClientError):
    pass

class PrivateError(ClientError):
    """For Private API"""

class BadCredentials(PrivateError):
    pass

class OnlyContainLetters(PrivateError):
    pass

class LongString(PrivateError):
    pass

class EmailExists(PrivateError):
    pass

class UsernameExists(PrivateError):
    pass

class NameExists(PrivateError):
    pass

class PlayListExists(PrivateError):
    pass

class WrongId(PrivateError):
    pass

class DuplicatePasswords(PrivateError):
    pass
    
class UnknownError(PrivateError):
    pass

