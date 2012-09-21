---
title: external/v2/json/removePlaylist
layout: method
---
## external/v2/json/removePlaylist

HTTPMethod: GET/POST
Required Parameters: playlist_uuid
Optional Parameters:

Removes the playlist with the specified UUID.

### Required Parameters
`
playlist_uuid:  UUID of the user. Must exist in the organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the playlist_uuid parameter.

`/external/v2/json/removePlaylist/`

### Response

On success a 200 status code, and a success status in JSON.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Permission Denied" 
    }
