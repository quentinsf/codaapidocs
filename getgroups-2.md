---
title: external/v2/json/getGroups
layout: method
---
## external/v2/json/getGroups

**HTTPMethod**: GET/POST

**Required Parameters**: 

**Optional Parameters**: name, group_uuid


Returns details either all users, or those that match the optional parameters.

### Optional Parameters

    group_uuid: Restrict groups to the one with the matching UUID.
    name:  Restrict groups to those that contain this string in their name (case insensitive).

### Usage

Simply send a GET or POST request with suitable OAuth credentials and optionally any of the filters required.

`/external/v2/json/getGroups/`

### Response

On success a 200 status code, and JSON encoded list of details about each group.

    name: The group's name.
    group_uuid: The group's UUID
    members: A list of UUIDs of the user who are members of this group.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "name": "Content managers",
            "group_uuid": "3c554dfe-f094-5f7e-0023-000000bf21fb",
            "members": "['3c554dfe-f094-5f7e-0021-0000000000ca']"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Invalid UUID" 
    }
