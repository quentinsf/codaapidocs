---
title: external/v2/json/uploadSource
layout: method
---
## external/v2/json/uploadSource

**HTTPMethod**: GET/POST

**Required Parameters**: name

**Optional Parameters**: replace, tags


Uploads source content with the given name, and optionally, tags and whether to replace an existing source.

### Required Parameters

    name: The name of the source content (e.g. "Monthly sales figures")

### Optional Parameters

    replace: Boolean value, which if 'true' and specified, replaces existing content of the same name.
    tags: A JSON-encoded array of tags for this uploaded content.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name, tags and replace flag.

`/external/v2/json/uploadSource/`

### Response

On success a 200 status code, along with the source_uuid of the uploaded content.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "source_uuid": "3c554dfe-f094-5f7e-0010-000000000001"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Permission Denied"·
    }
