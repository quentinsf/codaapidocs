---
title: external/v2/json/createDisplay
layout: method
---
## external/v2/json/createDisplay

HTTPMethod: GET/POST

Required Parameters: serial

Optional Parameters: 


Allows you to register hardware devices with the given serial number. 

### Required Parameters

    serial: The serial number of the hardware device. Must be a valid, unregistered, serial number.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and the serial parameter.

`/external/v2/json/createDisplay/`

### Response

On success a 200 status code,  along with the UUID of the new display.

    display_uuid: UUID of the newly registered display.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "display_uuid": "3c554dfe-f094-5f7e-0003-000000000001"
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Permission denied" 
    }