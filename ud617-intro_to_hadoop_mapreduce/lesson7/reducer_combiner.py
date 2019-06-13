#!/usr/bin/env python

import sys

count = 0
totalValue = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", float(1.0*totalValue/(1.0*count))
        oldKey = thisKey
        totalValue = 0
        count = 0

    oldKey = thisKey
    totalValue += float(thisValue)
    count += 1

if oldKey:
    print oldKey, "\t", float(1.0*totalValue/(1.0*count))
