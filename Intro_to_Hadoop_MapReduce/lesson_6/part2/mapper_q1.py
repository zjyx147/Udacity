#!/usr/bin/env python

import sys

for line in sys.stdin:
  start = line.find("GET ")
  end =  line.find("HTTP")
  res = line[start+4:end]
  print "{0}".format(res)
