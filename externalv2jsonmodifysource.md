---
title: external/v2/json/modifySource
---
## external/v2/json/modifySource

HTTPMethod: GET/POST
Required Parameters: source_uuid
Optional Parameters: name, parameters

Allows you to modify a source item to change the name and/or associated parameters. In CODA, each source type you see is has a corresponding UUID for the type, and a set of required and optional parameters. Full details on the source types can be found [here](/faqs/api/source-types-and-the-api).

### Required Parameters

    source_uuid: The UUID of the source type you wish to create.

### Optional Parameters

    name: The name for the source.
    parameters: a JSON encoded dictionary of parameters for that source.
    scaling: a string - set to one of NONE, FIT, CROP, STRETCH to control how/whether content gets resized to fit available display space.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the source_uuid, name and parameters.

`https://api.codaview.com/external/v2/json/modifySource/`

### Response

On success a 200 status code.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Permission denied" 
    }
