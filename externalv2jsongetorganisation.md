---
title: external/v2/json/getOrganisation
layout: method
---
## external/v2/json/getOrganisation

HTTPMethod: GET/POST
Required Parameters: 
Optional Parameters: 

Returns details about the organisation associated with the OAuth token used in the request.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name parameter.

`https://api.codaview.com/external/v2/json/getOrganisation/`

### Response

On success a 200 status code, along with a success code.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "organistaion_uuid": "blah",
            "name": "My Org"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Cannot modify group" 
    }