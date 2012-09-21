---
title: API Authentication
layout: method
---
## Overview

Authentication with the CODA API is carried out using the open [OAuth](http://oauth.net/) standard, and libraries exist to carry out the OAuth protocol [for most common languages](http://oauth.net/code/). The OAuth standard is designed to provide a way for third party applications to make use of a particular API on behalf of a user without that user having to give the third party their personal login credentials for the site in question. It is primarily designed to allow interactions between web services, but can also be used by desktop or mobile applications.

To use the OAuth API each application requires a Consumer Key/Secret pair authorised by the CODA system. You can create and manage your Consumers Keys by logging into CODA and visiting [CODA Dev Central](https://www.codaview.com/gui/developer/).

## OAuth Authorization URLs

CODA uses common standard locations for OAuth authentication:

    /oauth/request_token/
    /oauth/authorize/
    /oauth/access_token/

<br/>
Use these URLs with a standard OAuth library to generate a validated access token for your application. After that you can access each API call using the URL specified on each page of the documentation. 

## Authentication and Organisations

Unlike most web services, where your application authenticates to carry out actions on behalf of a particular user, in CODA user operations are done within the context of a particular organisation. All content and CODA hardware is actually owned by an organisation rather than a user, and users simply have permission to use the resources of a particular organisation.

As such, when a CODA user approves an OAuth authentication request from an application, they do so not only for that particular user, but for that particular user in a particular organisation. As a consequence, if a user wants to authenticate the application for use in multiple organisations, they must do so once for each organisation.

The reason this limit is imposed is to allow remote applications to understand the concept of CODA organisations, and potentially expose that in their own user interface. Your application can query CODA about the organisation information associated with a given access token. You could potentially use this as a way to let users from the same CODA organisation share data on your application.