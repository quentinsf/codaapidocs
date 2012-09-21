---
title: external/v2/json/createGroup
layout: method
---
## external/v2/json/createGroup

HTTPMethod: GET/POST
Required Parameters: name
Optional Parameters:

Creates a new user group with the specified name.

### Required Parameters
`
name:  Name of the group. Must be unique in this organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name parameter.

`/external/v2/json/createGroup/`

### Response

On success a 200 status code, along with the UUID of the newly created group.

`
group_uuid: The unique identifier for the group.
`

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "group_uuid": "3c554dfe-f094-5f7e-0023-000000000001"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot create group" 
    }