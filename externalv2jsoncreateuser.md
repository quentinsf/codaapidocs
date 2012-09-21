---
title: external/v2/json/createUser
---
## external/v2/json/createUser

HTTPMethod: GET/POST
Required Parameters: username, password, first_name, last_name, email, permission
Optional Parameters:

Creates the user specified, allowing you to specify the user's name, password, email address or permission level.

### Required Parameters

    username:  New name of the user. Must be globally unique.
    password: New password of the user.
    first_name: New first name of the user.
    last_name: New last name of the user.
    email: New email address of the user.
    permission: New permission level of the user.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the username, password, first_name, last_name, email and permission parameters.

`https://api.codaview.com/external/v2/json/createUser/`

### Response

On success a 200 status code, along with the UUID of the newly created user.

`
user_uuid: The unique identifier for the user.
`

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "user_uuid": "3c554dfe-f094-5f7e-0022-000000000001"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot create user" 
    }
