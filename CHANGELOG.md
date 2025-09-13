# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## 0.6.0
*2025-09-13*

- Updated models based on latest RJ API
- Updated dependencies

## 0.5.0
*2023-03-19*

- Fixed media-id extractor from url
- Removed get_popular_artists() method

## 0.4.0
*2023-01-14*

- Added account_notifications() method
- Added account_notifications_update() method
- Updated headers & domain based on latest version of app

## 0.3.0
*2022-02-04*

- Added signup() method
- Added save_session() method
- Added load_session() method
- Updated headers & domain based on latest version of app

## 0.2.2
*2021-08-26*

- Added User model
- Added get_user_by_url() method
- Added get_user_by_username() method
- Added get_user_followers() method
- Added get_user_following() method
- Added follow_user() method
- Added unfollow_user() method
- Added my_followers() method
- Added my_following() method
- Added bio argument to account_edit() method
- Changed name of Profile model to ShortUser
- Changed name of attribute from profiles to users in SearchResults model
- Changed name of my_following() [old method] to following_artists() method
- Fixed unclosed file in upload_photo() by using context manager

## 0.2.0
*2021-08-24*

- Added ShortData and MyPlaylists models
- Added logout() method for clean logout
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
- Fixed bug in url_to_id() [ When url contains "(" or ")" ]
- Fixed bug in change_password() [ Now updates cookies ]
- Fixed bug in change_photo()
- Fixed bug in remove_photo()
- Fixed bug in get_artist_by_name() by encoding url params via quote_plus 

## 0.1.1
*2021-02-21*

- Added RadioJavan tv and radio.

## 0.1.0
*2021-02-08*

- Initial release
