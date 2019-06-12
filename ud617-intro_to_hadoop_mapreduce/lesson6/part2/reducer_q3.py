#!/usr/bin/env python

import sys

maxHits = 0
totalHits = 0
maxKey = None
oldKey = None

for line in sys.stdin:
  thisKey = line.strip().split("\t")
  if len(thisKey) != 1:
    continue

  if oldKey and oldKey != thisKey:
    print oldKey, "\t", totalHits
    if totalHits > maxHits:
      maxHits = totalHits
      maxKey = oldKey
    totalHits = 0

  oldKey = thisKey
  totalHits += 1

if oldKey:
  print oldKey, "\t", totalHits
  if totalHits > maxHits:
    maxHits = totalHits
    maxKey = oldKey

print "{0}\t{1}".format(maxKey, maxHits)   
