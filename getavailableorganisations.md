---
title: external/v2/json/getAvailableOrganisations
layout: method
---
## external/v2/json/getAvailableOrganisations

**HTTPMethod**: GET/POST

**Required Parameters**: 

**Optional Parameters**: 

Returns details about the organisations associated with the OAuth token used in the request.  If this was created with the default 
'organisation' scope, the result will be a list containing just one
organisation.

If, however, the scope used was 'impersonate', it will include
all the orgs of which the user is a member, and if any child orgs
over the user has reseller permissions.  See the [API Authentication](api-authentication) documentation for more info.

### Usage

Simply send a GET or POST request with suitable OAuth credentials.

`/external/v2/json/getAvailableOrganisations/`

### Response

On success a 200 status code, along with a success code.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": [
            {
                "organisation_uuid": "blah",
                "name": "My Org"
            },
            {
                "organisation2_uuid": "blah2",
                "name": "My Other Org"
            },
        ]
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Reason for failure" 
    }