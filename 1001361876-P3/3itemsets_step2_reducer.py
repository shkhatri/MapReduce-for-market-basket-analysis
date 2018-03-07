#!/usr/bin/env python

import sys

for line in sys.stdin:

     line = line.strip()
     part1,part2,part3 = line.split('\t', 2)
     # if B and C part of 3itemsets (B C A) is present in 2itemsets
     if part3 != '1':
         print('%s\t%s\t%s' % (part3,part1,part2))
    