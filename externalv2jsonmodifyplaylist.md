---
title: external/v2/json/modifyPlaylist
---
## external/v2/json/modifyPlaylist

HTTPMethod: GET/POST
Required Parameters: playlist_uuid, uuid_duration_mapping
Optional Parameters:

Modifies the playlist specified.  Replaces its contents with the contents of uuid_duration_mapping.

### Required Parameters

    playlist_uuid:  UUID of the playlist to be modified.
    uuid_duration_mapping: Ordered list of dictionaries, with:
          source_uuid: source UUID for this content
          duration:  duration for this source

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the playlist_uuid and uuid_duration_mapping parameters.

`https://api.codaview.com/external/v2/json/modifyPlaylist/`

### Response

On success a 200 status code, along with a success parameter.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK"
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot modify playlist" 
    }
