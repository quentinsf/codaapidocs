---
title: external/v2/json/touchSource
layout: method
---
## external/v2/json/touchSource

**HTTPMethod**: GET/POST

**Required Parameters**: source_uuid

Optional Parameters:·

Updated the last-modified time for a source with the given UUID.

### Required Parameters

    source_uuid: The UUID of the source to be updated.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the source UUID.

`/external/v2/json/touchSource/`

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
        "error": "Permission Denied"·
    }
