---
title: external/v2/json/modifyUser
layout: method
---
## external/v2/json/modifyUser

**HTTPMethod**: GET/POST

**Required Parameters**: user_uuid

**Optional Parameters**: username, password, first_name, last_name, email, permission


Updates the user specified with the provided UUID, allowing you to change the user's name, password, email address or permission level. Only those parameters provided will be updated.

### Required Parameters

    user_uuid: The UUID of the user to be modified.

### Optional Parameters

    username:  New name of the user. Must be globally unique.
    password: New password of the user.
    first_name: New first name of the user.
    last_name: New last name of the user.
    email: New email address of the user.
    permission: New permission level of the user.

### Usage

Simply send a GET or POST request with suitable OAuth credentials, the user's UUID, and the parameters which
you wish to update.

`/external/v2/json/modifyUser/`

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
        "error": "Cannot modify user" 
    }
