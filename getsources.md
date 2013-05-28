---
title: external/v2/json/getSources
layout: method
---
## external/v2/json/getSources

**HTTPMethod**: GET/POST

**Required Parameters**: 

**Optional Parameters**: name, source_uuid, type_uuids


Returns details either all displays, or those that match the optional parameters.

### Optional Parameters

    source_uuid: Restrict sources to the one with the matching UUID.
    source_uuids: Restrict sources to the ones in this list of UUIDs.
    name:  Restrict sources to those that contain this string in their name (case insensitive).
    type_uuids: a JSON encoded list of source type UUIDs. Restricts sources to those matching the specified types.

### Usage

Simply send a GET or POST request with suitable OAuth credentials and optionally any of the filters required.

`/external/v2/json/getSources/`

### Response

On success a 200 status code, and JSON encoded list of details about each source.

    name: The content source's name.
    source_uuid: The UUID of this content source.
    valid_from: The date and time the content source is valid from
    valid_until: The date and time the content source is valid until
    tags: A list of tags for this content source
    type_name: A textual description of this content type
    type_uuid: The UUID of the type of this content source. 
    last_modified: The time and date this content was last modified
    date_added: The time and date this content was added
    creator: The textual name of the creator of this content source
    default_duration: The duration of this content source will be displayed for 
    parameters: A list of parameters which vary according to the type of content. For example, for a web page, 'url' is one of the parameters.
                
On failure a 200 status code, along with a description of the error.

### Example Successful JSON Response

    {
        "result": "OK",
        "response": [
            {
                "name": "BBC News Frontpage",
                "source_uuid": "3c554dfe-f094-5f7e-0010-00000000808d",
                "valid_until": 'None',
                "valid_from": 'None',
                "tags": ['news', 'current events'],
                "type_name": 'RSS Feed',
                "type_uuid": '3c554dfe-f094-5f7e-0013-00000000000a', 
                "last_modified": '2010-04-26 10:07:26',
                "date_added": '2010-03-01 09:50:50',
                "creator": 'jbloggs',
                "default_duration": '30 seconds',
                "parameters": {
                      'url': 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
                      "images": True,
                      "theme": 'ORIGINAL'
                 }
            }, { ...further dictionaries... }
        ]
    }

### Example Unsuccessful JSON Response

    {
        "result": "FAIL",
        "error": "Invalid UUID" 
    }
