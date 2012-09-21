---
title: external/v2/json/getDisplays
layout: method
---
## external/v2/json/getDisplays

HTTPMethod: GET/POST

Required Parameters: 

Optional Parameters: name, serial, owner_uuid, site_uuid, display_uuid


Returns details either all displays, or those that match the optional parameters.

### Optional Parameters

    display_uuid: Restrict displays to the one with the matching UUID.
    display_uuids: Restrict displays to the ones in this list of UUIDs.
    name:  Restrict displays to those that contain this string in their name (case insensitive).
    serial: Restrict displays to the one with the matching serial number.
    owner_uuid: Restrict displays to those where the owner matches the specified UUID.
    site_uuid: Restrict displays to those where the site matches the specified UUID.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and optionally any of the filters required.

`/external/v2/json/getDisplays/`

### Response

On success a 200 status code, and JSON encoded list of details about each display.

    name: The display's name.
    display_uuid: The UUID that identifies this display.
    mode: The current mode the display is set to.
    mode_list: The list of valid modes for this display, as reported over EDID.
    tags: A list of tags for this display.
    site_uuid: The UUID of the site in which this display is located.
    owner_uuid: The owner of the display, if one is specified.
    ip_address: The last know IP address of this display.
    is_active: Whether the display was online when the API call was made.
    serial: The serial number of the display (for CODApods, this is also its Ethernet MAC address).
    last_seen: The time at which the display last requested information from Camvine's servers.
    rotation: The logical orientation of the display.
    source_uuid: The UUID of the piece of content currently being played, or null if the display is blank.
    up_to_date: Has the display reacted to the last content assignment action.

Note that the latitude and longitude parameters can only currently be set by the API, and are not automatically update by the CODApod.

On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": {
            "name": "My display",
            "display_uuid": "blah",
            "mode": "1024x768@60",
            "mode_list": "1280x1024@60 1024x768@60",
            "tags": ["foo", "bar"],
            "site_uuid": "blah",
            "owner_uuid": null,
            "ip_address": "192.168.1.10",
            "is_active": true,
            "serial": "112233445566",
            "last_seen": "2010-04-23 10:37:03.415243",
            "rotation": "90",
            "source_uuid": null,
            "up_to_date": true
        }
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Invalid UUID" 
    }