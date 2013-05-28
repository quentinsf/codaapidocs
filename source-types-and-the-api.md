---
title: Source Types and the API
layout: method
---
When mutating sources in CODA  via the API you need to know a few things, depending on what you're trying to do. Firstly, to create a Source, you need to know the UUID of the SourceType (though there are some helper functions for common sources). You also need to know what parameters that source type expects you to provide. This page gives you an overview of this.

The below list shows you a list of source types applications can general create and modify. Note that it is possible we may restrict applications to a set of types we think is appropriate. If you have particular needs for a given source type, let us know, and we'll ensure you can access that type.

<table width="100%" border="0">
<tr>
<th>Source icon</th>
<th>Source Type</th>
<th>UUID</th>
<th>Parameters</th>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_markup_bm.png" />
		</td>
<td>
			CODA Markup Document
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000008
		</td>
<td>
<ul>
<li>url: URL of CML page
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_flash_bm.png" />
		</td>
<td>
			Flash
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000013
		</td>
<td>
<ul>
<li>url: URL of Flash SWF file
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_html_bm.png" />
		</td>
<td>
			HTML page
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000010
		</td>
<td>
<ul>
<li>url: URL of web page
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_onlinecalendar_bm.png" />
		</td>
<td>
			iCal Calendar
		</td>
<td>
			3c554dfe-f094-5f7e-0013-00000000000c
		</td>
<td>
<ul>
<li>url: URL of iCal Calendar
</li>
<li>theme: The theme of the calendar
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_image_bm.png" />
		</td>
<td>
			Image
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000001
		</td>
<td>
<ul>
<li>url: URL of image
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_pdf_bm.png" />
		</td>
<td>
			PDF
		</td>
<td>
			3c554dfe-f094-5f7e-0013-00000000000d
		</td>
<td>
<ul>
<li>url: URL of PDF file
</li>
<li>pdf_duration: Duration of each page
</li>
<li>pdf_page: Page number, or blank for all pages
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_imageplaylist_bm.png" />
		</td>
<td>
			Photocast
		</td>
<td>
			3c554dfe-f094-5f7e-0013-00000000000b
		</td>
<td>
<ul>
<li>url: URL of photocast
</li>
<li>duration: Duration for each entry
</li>
<li>random: Duration for each entry
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_mixedplaylist.png" />
		</td>
<td>
			Playlist
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000003
		</td>
<td>
<ul>
<li>randomize: Play the album in a random order
</li>
<li>caption_duration: How long image captions should be displayed
</li>
<li>caption_style: Style of captions displayed
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_rss_bm.png" />
		</td>
<td>
			RSS Feed
		</td>
<td>
			3c554dfe-f094-5f7e-0013-00000000000a
		</td>
<td>
<ul>
<li>url: URL of RSS Feed
</li>
<li>images: Show images in feed
</li>
<li>theme: The theme of the RSS feed
</li>
</ul>
</td>
</tr>
<tr>
<td>
			<img src="https://console.envisage-system.co.uk/static/gui/icons/icon_video_bm.png" />
		</td>
<td>
			Video
		</td>
<td>
			3c554dfe-f094-5f7e-0013-000000000015
		</td>
<td>
<ul>
<li>url: URL of video
</li>
</ul>
</td>
</tr>
</table>