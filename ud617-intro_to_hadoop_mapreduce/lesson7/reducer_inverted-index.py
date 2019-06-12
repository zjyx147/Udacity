#!/usr/bin/env python

import sys
import csv
import string

count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisValue = data_mapped
    if thisKey == 'fantastically':
        print thisKey, "\tnode_id:", thisValue
    if oldKey and oldKey != thisKey:
        print thisKey, "\t", count
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += 1

if oldKey:
    print oldKey, "\t", count
