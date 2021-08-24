# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## 0.2.0
*2021-08-24*

- Added ShortData and MyPlaylists models
- Added logout method for clean logout
- Added new exceptions
- Removed ComingSoon model and get_coming_soon() method
- Changed name of some exceptions
- Changed headers to latest app version
- Changed SearchResults structure by adding ShortData
- Changed models to latest RadioJavan API.
- Changed account_edit() arguments from dict to separate str
- Changed my_playlists() return object from dict to MyPlaylists
- Changed arguments of actions methods (like, follow, ...) from Object to media id or artist name
- Changed arguments of create, rename and delete playlists methods from Object to ids
- Changed arguments of add or remove a song/video methods from Object to ids
- Fixed bug in url_to_id() (When url contains '(' or ')')
- Fixed bug in change_password() (Now update cookies)
- Fixed bug in change_photo()
- Fixed bug in remove_photo()
- Fixed bug in get_artist_by_name() by encoding url params via quote_plus 

## 0.1.1
*2021-02-21*

- Added RadioJavan tv and radio.

## 0.1.0
*2021-02-08*

- Initial release
