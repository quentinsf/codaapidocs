---
title: external/v2/json/createSources
layout: method
---
## external/v2/json/createSources

**HTTPMethod**: GET/POST

**Required Parameters**: sources_info

**Optional Parameters**: 


Allows you to create multiple new source items with specified types and associated parameters. This effectively allows multiple [createSource](createsource.html) calls to be made in one single call.

### Required Parameters
    sources_info: a JSON-encoded list of source info. Each entry should be a dictionary containing parameters as accepted by createSource:
    - name
    - type_uuid
    - parameters
    - scaling
    - duration (optional)
    - tags (optional)

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the sources_info parameter.

`/external/v2/json/createSources/`

### Response

On success a 200 status code,  along with the UUID of the new source.

    source_uuids: UUIDs of the newly created source.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "source_uuids": [
              "3c554dfe-f094-5f7e-0010-000000000001", 
              "3c554dfe-f094-5f7e-0010-000000000002"]
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Permission denied" 
    }