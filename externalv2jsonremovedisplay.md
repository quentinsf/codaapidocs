---
title: external/v2/json/removeDisplay
---
## external/v2/json/removeDisplay

HTTPMethod: GET/POST
Required Parameters: display_uuid
Optional Parameters:

Removes the display with the specified UUID.

### Required Parameters
`
display_uuid:  UUID of the display. Must exist in the organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the display_uuid parameter.

`https://api.codaview.com/external/v2/json/removeDisplay/`

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