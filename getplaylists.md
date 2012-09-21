---
title: external/v2/json/getPlaylists
layout: method
---
## external/v2/json/getPlaylists

HTTPMethod: GET/POST

Required Parameters: 

Optional Parameters: name, playlist_uuid


Returns details either all playlists, or those that match the optional parameters.

### Optional Parameters

    playlist_uuid: Restrict playlists to the one with the matching UUID.
    name:  Restrict playlists to those that contain this string in their name (case insensitive).

### Usage

Simply send a GET or POST request with suitable OAuth credentials and optionally any of the filters required.

`/external/v2/json/getPlaylists/`

### Response

On success a 200 status code, and JSON encoded list of details about each playlists.

    playlist_name: The playlist's name.
    playlist_uuid: This playlist's UUID.
    playlist_sources: A list of sources in this playlist, with each containing a source_uuid, source_duration and source_name key.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
              'playlist_name': 'another playlist'}
              'playlist_uuid': '3c554dfe-f094-5f7e-0010-00000000841d',
              'playlist_sources': [ {
                           'source_uuid': '3c554dfe-f094-5f7e-0010-00000000808d',
                           'source_duration': '30 seconds',
                           'source_name': 'BBC News Frontpage'} ],
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Invalid UUID" 
    }
