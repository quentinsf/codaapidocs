#! /usr/bin/env python

import json, os, getpass

if getpass.getuser() == 'mozz':
  work_dir = "/Users/mozz/Dropbox/files/work/Telemarq/Telemarq_shared/api_docs_json"
else:
  work_dir = "/Users/qsf/Dropbox/Telemarq/Telemarq_shared/api_docs_json"

out_dir = "."

for fname in os.listdir(work_dir):
    if fname.endswith(".json"):
        with open(os.path.join(work_dir, fname), 'r') as i:
            data = i.read()
            data = json.loads(data)
            link = data['permalink']
            body = data['body']
            with open(os.path.join(out_dir, "%s.md" % link), 'w') as o:
                # Write the header part of the output file
                o.write("""---
title: %s
layout: method
---
""" % data['title'])
                # Look for things that appear to be hrefs and convert them so they work
                body = body.replace("/faqs/api/","")
                o.write(body.encode("UTF-8"))

print "Done"
