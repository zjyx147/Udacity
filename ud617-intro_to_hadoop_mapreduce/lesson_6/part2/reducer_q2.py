#!/usr/bin/env python

import sys

totalHits = 0
oldKey = None

for line in sys.stdin:
  thisKey = line.strip().split("\t")
  if len(thisKey) != 1:
    continue

  if oldKey and oldKey != thisKey:
    print oldKey, "\t", totalHits
    totalHits = 0

  oldKey = thisKey
  totalHits += 1

if oldKey:
  print oldKey, "\t", totalHits
