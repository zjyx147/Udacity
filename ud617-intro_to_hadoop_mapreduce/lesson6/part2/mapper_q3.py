#!/usr/bin/env python

import sys

for line in sys.stdin:
  data = line.split()
  if len(data) == 10:
    ip, id, user, datetime, timezone, method, path, proto, status, size = data
    #filename = path.split('/')[-1]
    newpath = path.replace("http://www.the-associates.co.uk/", "").lstrip('/')
    print '/'+newpath
