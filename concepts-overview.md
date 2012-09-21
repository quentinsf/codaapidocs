---
title: Concepts Overview
---
To use the API you need to be familiar with a few core concepts related to the CODA platform. Here we give you a brief overview of these concepts, and assume that you are familiar with the basic operations the traditional CODA UI affords.

## Users

A User is someone who is registered with CODA and is a member of at least one Organisation. When API calls are made, they are made on behalf of a particular user.

## Organisations

Each User in CODA is a member of one or more Organisations. An Organisation is the entity to which content and hardware resources belong. Users who are members of an Organisation can access those resources belonging to the Organisation.

## Displays

The hardware that CODA provides is used to drive screens, regardless of product line, is abstracted as the notion of a Display. A display is a device to which content can be assigned. If no content is assigned, then the display will power off.

## Sources

A Source is a single piece of displayable content in the CODA system. To display some piece of content on a CODA Display, it must first be added to the CODA platform as a Source. Sources can represent a number of things:

* content linked to by a URL that resides on a network somewhere
* a file that has been uploaded to CODA's content delivery network
* some special sources combine a number of other sources, eg. Playlists or Screen Schedules.

Sources have a type associated with them (e.g., Image, PDF, or Video). Each type will have a number of parameters that need to be filled in. A list of Source types, the UUID by which to refer to them, and the parameters they take can be found in the <a href="/faqs/api/source-types-and-the-api">Source Types</a> section of this documentation.

## Playlists

Playlists are a special type of source that can be used to contain and organise other Sources (including other Playlists). A Source in a playlist has a position and a duration associated with it that defines how the Playlist plays.

## Groups

Users can be placed together in a group. This is used for defining who can assign content to displays.

## Sites

Sites are collections of displays. All displays are in one site, and one site only. In addition to being a useful way to group displays, Sites have an associated timezone, which is used in scheduling to work out what should show on the screen at what time.