#! /usr/bin/env python

import json, os, getpass
import re

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
            link = data['permalink'].replace('externalv2json', '').replace('externalv2son', '')
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
                
                body = re.sub(r'^(HTTPMethod: .*)$', r"\1\n", body, flags=re.MULTILINE)
                body = re.sub(r'^(Required Parameters: .*)$', r"\1\n", body, flags=re.MULTILINE)
                body = re.sub(r'^(Optional Parameters: .*)$', r"\1\n", body, flags=re.MULTILINE)

                o.write(body.encode("UTF-8"))

with open(os.path.join(out_dir, "_includes", "sitemap.html"), 'w') as o:
  o.write("<ul id='sitemap'>")
  o.write("\n    <li><a href='.'>Home</a></li>")
  for n in range(0, len(titles) - 1):
    o.write("\n    <li><a href='%s'>%s</a></li>" % (links[n], titles[n].replace("external/v2/json/", "")) )
  o.write("\n</ul>")

print "Done"
