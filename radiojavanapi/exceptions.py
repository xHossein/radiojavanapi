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

class InvalidName(PrivateError):
    pass

class LongString(PrivateError):
    pass

class EmailExists(PrivateError):
    pass

class UsernameExists(PrivateError):
    pass

class DuplicateName(PrivateError):
    pass

class InvalidMediaId(PrivateError):
    pass

class DuplicatePassword(PrivateError):
    pass
    
class UnknownError(PrivateError):
    pass

