---
title: external/v2/json/removeUser
---
## external/v2/json/removeUser

HTTPMethod: GET/POST
Required Parameters: user_uuid
Optional Parameters:

Removes the user with the specified UUID.

### Required Parameters
`
user_uuid:  UUID of the user. Must exist in the organisation.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the user_uuid parameter.

`https://api.codaview.com/external/v2/json/removeUser/`

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
