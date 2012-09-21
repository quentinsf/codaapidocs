---
title: external/v2/json/createPlaylist
layout: method
---
## external/v2/json/createPlaylist

**HTTPMethod**: GET/POST

**Required Parameters**: name, uuid_duration_mapping

Optional Parameters:

Creates the playlist specified, allowing you to specify the playlist's name and content.

### Required Parameters

    name:  Name of the playlist to be created. Must be organisationally unique.
    uuid_duration_napping: Ordered list of dictionaries, with:
          source_uuid: source UUID for this content
          duration:  duration for this source

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name and uuid_duration_mapping parameters.

`/external/v2/json/createPlaylist/`

### Response

On success a 200 status code, along with the UUID of the newly created playlist.

`
playlist_uuid: The unique identifier for the playlist.
`

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "playlist_uuid": "3c554dfe-f094-5f7e-0010-000000000011"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot create playlist" 
    }
