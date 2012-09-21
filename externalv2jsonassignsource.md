---
title: external/v2/json/assignSource
layout: method
---
## external/v2/json/assignSource

HTTPMethod: GET/POST
Required Parameters: display_uuids, source_uuid
Optional Parameters: 

Assigns the source with the given UUID to run on the displays listed by UUID.

### Required Parameters

    source_uuid: The UUID of the source to be assigned.
    display_uuids: A JSON encoded list of displays to which the source is to be assigned.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the source UUID and display UUIDs.

`https://api.codaview.com/external/v2/json/assignSource/`

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
        "error": "Permission Denied" 
    }