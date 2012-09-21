---
title: external/v2/json/getSites
layout: method
---
## external/v2/json/getSites

HTTPMethod: GET/POST
Required Parameters: 
Optional Parameters: name, site_uuid

Returns details either all sites, or those that match the optional parameters.

### Optional Parameters

    site_uuid: Restrict sites to the one with the matching UUID.
    name:  Restrict sites to those that contain this string in their name (case insensitive).

### Usage

Simply send a GET or POST request with suitable OAuth credentials and optionally any of the filters required.

`/external/v2/json/getSites/`

### Response

On success a 200 status code, and JSON encoded list of details about each site.

    name: The site's name.
    site_uuid: This site's UUID.
    displau_uuids: A list of UUIDS of the displays belonging to this site.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": [{
            "name": "San Francisco office, CA",
            "site_uuid": "3c554dfe-f094-5f7e-0022-000000000116",
            "display_uuids": "['3c554dfe-f094-5f7e-0003-00000000027b', '3c554dfe-f094-5f7e-0003-0000000002fa']"
        }]
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Invalid UUID" 
    }
