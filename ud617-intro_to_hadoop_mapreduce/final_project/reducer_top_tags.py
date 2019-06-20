#!/usr/bin/python

import sys

topCount=[0]*10
topTag=[0]*10

for line in sys.stdin:

    data=line.strip().split('\t')
    
    if len(data) != 2:
        continue
    
    thisTag,thisCount = data
    
    min_count=min(topCount)
    min_index=topCount.index(min_count)
    
    if int(thisCount)>= min_count:
        topCount[min_index]=int(thisCount)
        topTag[min_index]=thisTag
        
# ...determine the sort order of the top-N
sort = sorted(range(N), key=lambda k: topCount[k], reverse=True)   
        
for i in range(0,10):
    print  "{0}\t{1}".format(topTag[sort[i]],topCount[sort[i]])
    
