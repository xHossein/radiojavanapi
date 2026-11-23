# Exceptions

## Common Exceptions
Exception | Base | Description
----------|------|------------
ClientError | Exception | Base exception for all RadioJavan calls
ClientJSONDecodeError | ClientError | Raised when the API response is not valid JSON
ClientConnectionError | ClientError | Raised on network connectivity issues
ClientLoginRequired | ClientError | Raised when a method requires you to be logged in


## Private Exceptions
Exception | Base | Description
----------|------|------------
PrivateError | ClientError | Base exception for private (authenticated) calls
BadCredentials | PrivateError | Raised when the email or password is wrong (login)
InvalidName | PrivateError | Raised when the first or last name contains digits (edit account)
LongString | PrivateError | Raised when a string is too long (edit account)
EmailExists | PrivateError | Raised when the email is already used by another account (edit account)
UsernameExists | PrivateError | Raised when the username is already used by another account (edit account)
DuplicatePassword | PrivateError | Raised when the new password is the same as the current one (edit account)
DuplicateName | PrivateError | Raised when a playlist with that name already exists (create or rename playlist)
InvalidMediaId | PrivateError | Raised when an invalid media id is provided (like, follow, ...)
InvalidEmail | PrivateError | Raised when an invalid email is provided
UnknownError | PrivateError | Raised when the API returns an unrecognized error message
