---
title: API Marshalling
layout: method
---
Requests are made to the API using either GET or POST parameters for the arguments, with complex parameters (lists and dictionaries) passed in JSON format. When referring to Sources and Displays in the API you must use their UUID.

All calls to valid API URLs will return with an HTTP 200 status. The result will be a JSON dictionary of information containing at most two things in the bottom level. The first item is always a result field, that will contain OK on success, or FAIL on failure. The second parameter, depending on the first, will be either: response, containing the information requested where appropriate, or error, containing a string describing why the call failed.