---
title: external/v2/json/createSource
layout: method
---
## external/v2/json/createSource

**HTTPMethod**: GET/POST

**Required Parameters**: name, type_uuid, parameters

**Optional Parameters**: 


Allows you to create a new source item with a specified type and associated parameters. In CODA, each source type you see is has a corresponding UUID for the type, and a set of required and optional parameters. Full details on the source types can be found [here](source-types-and-the-api).

### Required Parameters

    name: The name for the source.
    type_uuid: The UUID of the source type you wish to create.
    parameters: a JSON encoded dictionary of parameters for that source.
    scaling: a string - set to one of NONE, FIT, CROP, STRETCH to control how/whether content gets resized to fit available display space.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the name, type UUID, and parameters.

`/external/v2/json/createSource/`

### Response

On success a 200 status code,  along with the UUID of the new source.

    source_uuid: UUID of the newly created source.

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
        "error": "Permission denied" 
    }