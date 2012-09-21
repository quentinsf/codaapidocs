---
title: external/v2/json/getUser
---
## external/v2/json/getUser

HTTPMethod: GET/POST
Required Parameters: 
Optional Parameters:

Returns details of the current user as identified by the API access token.

### Usage

Simply send a GET or POST request with suitable OAuth credentials.

`https://api.codaview.com/external/v2/json/getUser/`

### Response

On success a 200 status code, and JSON encoded list of details about the user.

    user_uuid: The UUID of this user.
    username: The CODA username of this user.
    first_name: The user's first name
    last_name: The user's last name
    email: The user's email address
                
A failure is likely to indicate a more serious problem.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
             "username": "gwb", 
             "first_name": "George", 
             "last_name": "Bush", 
             "user_uuid": "3c664dfe-f094-5f7e-0021-000000000009", 
             "email": "georgie@allgone.com"
         }
    }


