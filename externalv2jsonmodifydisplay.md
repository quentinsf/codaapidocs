---
title: external/v2/json/modifyDisplay
layout: method
---
## external/v2/json/modifyDisplay

HTTPMethod: GET/POST
Required Parameters: display_uuid
Optional Parameters: name, mode, rotation, tags, owner_uuid

Updates the display specified with the provided UUID, allowing you to change the display's name, mode, rotation, tags, and owner. Only those parameters provided will be updated.

### Required Parameters

    display_uuid: The UUID of the display to be modified.

### Optional Parameters

    name:  New name of the display. Must be unique within the organisation.
    mode: A mode string for the display - should be taken from the mode_list for the display in question.
    rotation: One of 0, 90, 180, 270. Other values are ignored.
    tags: A JSON encoded list of tags the display should have. The list here will replace the previous list.
    owner_uuid: The UUID of a user or group that is allowed to control the display. 

### Usage

Simply send a GET or POST request with suitable OAuth credentials, the display's UUID, and the parameters which you wish to update.

`https://api.codaview.com/external/v2/json/modifyDisplay/`

### Response

On success a 200 status code, along with a success code.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot modify display" 
    }