---
title: external/v2/json/modifyGroup
layout: method
---
## external/v2/json/modifyGroup

**HTTPMethod**: GET/POST

**Required Parameters**: group_uuid

**Optional Parameters**: name, members


Updates the group specified with the provided UUID, allowing you to change the group's name and members.

### Required Parameters

    group_uuid: The UUID of the group to be modified.


### Optional Parameters

    name:  New name of the group. Must be unique in this organisation.
    members: A JSON encoded list of members for this group. The previous list of members will be replaced with this one if specified.
`

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name parameter.

`/external/v2/json/modifyGroup/`

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
        "error": "Cannot modify group" 
    }