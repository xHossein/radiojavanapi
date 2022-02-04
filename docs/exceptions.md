# Exceptions

## Common Exceptions
Exception | Base | Description
----------|------|------------
ClientError | Exception | Base Exception for RadioJavan calls
ClientJSONDecodeError | ClientError | JSON Exception
ClientConnectionError | ClientError | Raised due to network connectivity-related issues
ClientLoginRequired | ClientError | Raised when RadioJavan required Login


## Private Exceptions
Exception | Base | Description
----------|------|------------
PrivateError | ClientError | Base Exception for Private calls
BadCredentials | PrivateError | Raised when email or password is wrong (login)
InvalidName | PrivateError | Raised when firstname or lastname contains digits (edit account)
LongString | PrivateError | Raised when string is too long (edit account)
EmailExists | PrivateError | Raised when email used by another account (edit account)
UsernameExists | PrivateError | Raised when username used by another account (edit account)
DuplicatePassword | PrivateError | Raised when a duplicate password is provided (edit account)
DuplicateName | PrivateError | Raised when a duplicate name is provided for playlist (create or rename playlist)
InvalidMediaId | PrivateError | Raised when an invalid media id is provided (like, follow, ...)
InvalidEmail | PrivateError | Raised when an invalid email is provided
UnknownError | PrivateError | Raised when get unknown message (new message from radiojavan)