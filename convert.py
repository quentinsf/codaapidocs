#! /usr/bin/env python

import json, os

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
                o.write("""---
title: %s
---
""" % data['title'])
                o.write(body.encode("UTF-8"))

print "Done"
