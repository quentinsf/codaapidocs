---
title: external/v2/json/removeGroup
layout: method
---
## external/v2/json/removeGroup

HTTPMethod: GET/POST

Required Parameters: group_uuid

Optional Parameters:

Removes the group with the specified UUID.

### Required Parameters
`
group_uuid:  UUID of the group. Must exist in the organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the group_uuid parameter.

`/external/v2/json/removeGroup/`

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