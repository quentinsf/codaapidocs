#! /usr/bin/env python

import json, os, getpass

if getpass.getuser() == 'mozz':
  work_dir = "/Users/mozz/Dropbox/files/work/Telemarq/Telemarq_shared/api_docs_json"
else:
  work_dir = "/Users/qsf/Dropbox/Telemarq/Telemarq_shared/api_docs_json"

out_dir = "."

YAML_FRONT_MATTER="""---
title: %(title)s
layout: %(layout)s
---
"""

links = []
titles = []
for fname in os.listdir(work_dir):
    if fname.endswith(".json"):
        with open(os.path.join(work_dir, fname), 'r') as i:
            data = i.read()
            data = json.loads(data)
            link = data['permalink']
            body = data['body']
            title = data['title']
            links.append(link)
            titles.append(title)

            with open(os.path.join(out_dir, "%s.md" % link), 'w') as o:
                
                # Write the header part of the output file
                o.write(YAML_FRONT_MATTER % {
                  'title'  :  title,
                  'layout' : 'method',
                })

                # Look for things that appear to be hrefs and convert them so they work
                body = body.replace("/faqs/api/","")

                # Look for instances of api.codaview.com and remove
                body = body.replace("https://api.codaview.com", "")

                o.write(body.encode("UTF-8"))

with open(os.path.join(out_dir, "sitemap.md"), 'w') as o:
  o.write(YAML_FRONT_MATTER % {
    'title'  :  "List of all pages",
    'layout' : 'method',
  })
  o.write("\n* [Home](/codaapidocs)")
  for n in range(0, len(titles) - 1):
    o.write("\n* [%s](%s)" % (titles[n], links[n]) )

print "Done"
