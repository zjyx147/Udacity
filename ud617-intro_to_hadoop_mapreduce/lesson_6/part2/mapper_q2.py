#!/usr/bin/env python

import sys

for line in sys.stdin:
  res = line.split()[0]
  print "{0}".format(res)
