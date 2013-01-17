---
title: API Authentication
layout: method
---
## Overview

Authentication with the CODA API is carried out using the open [OAuth](http://oauth.net/) standard, and libraries exist to carry out the OAuth protocol [for most common languages](http://oauth.net/code/). The OAuth standard is designed to provide a way for third party applications to make use of a particular API on behalf of a user without that user having to give the third party their personal login credentials for the site in question. It is primarily designed to allow interactions between web services, but can also be used by desktop or mobile applications.

To use the OAuth API each application requires a Consumer Key/Secret pair authorised by the CODA system. You can create and manage your Consumers Keys by logging into CODA and visiting [CODA Dev Central](https://console.envisage-system.co.uk/gui/developer/).

## OAuth Authorization URLs

CODA uses common standard locations for OAuth authentication:

    /oauth/request_token/
    /oauth/authorize/
    /oauth/access_token/

Use these URLs with a standard OAuth library to generate a validated access token for your application. After that you can access each API call using the URL specified on each page of the documentation. 

## Authentication and Organisations

In CODA, user operations are done within the context of a particular organisation. All content and CODA hardware is actually owned by an organisation rather than a user, and users simply have permission to use the resources of a particular organisation.

As such, when a CODA user approves an OAuth authentication request from an application, they normally do so for that particular user _in a particular organisation_. As a consequence, if a user wants to authenticate the application for use in multiple organisations, they must do so once for each organisation.

### Impersonation

A recent update to the API, however, allows an app to request the ability to 'impersonate' a user, and so have access to any organisations to which that user would have access when logged in to CODA.

To do this, the app needs to request an access token with the 'scope' parameter set to 'impersonate' (the default is 'organisation').  The CODA web page through which the user approves the request will no longer ask them to select the organisation for which they are granting permission.

**IMPORTANT**:  Since the resulting token is not tied to any particular organisation, most calls which use it must therefore include an extra *organisation_uuid* parameter. Note that this is *not* shown in the documentation for individual calls.

A list of the organisations available to a user, and their UUIDs, can be retrieved using the '[getAvailableOrganisations](getavailableorganisations)' method.

