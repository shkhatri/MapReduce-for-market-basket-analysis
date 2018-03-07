#!/usr/bin/env python

import sys
current_count = 0


for line in sys.stdin:
	
     line = line.strip()
     part1,part2,part3 = line.split('\t', 2)
     # to make it in the required order
     print('%s\t%s\t%s' % (part2,part3,part1))