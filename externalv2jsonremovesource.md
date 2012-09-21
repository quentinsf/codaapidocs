---
title: external/v2/json/removeSource
layout: method
---
## external/v2/json/removeSource

HTTPMethod: GET/POST
Required Parameters: source_uuid
Optional Parameters:

Removes the source with the specified UUID.

### Required Parameters
`
source_uuid:  UUID of the source. Must exist in the organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the source_uuid parameter.

`https://api.codaview.com/external/v2/json/removeSource/`

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