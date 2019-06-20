#!/usr/bin/python

# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate a Hadoop cluster in our system :-)
# This will serve as a storage for your code.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 19:
        hour = int(line[8][11:13])
        author_id = line[3]
        print "{0}\t{1}".format(author_id, hour)
