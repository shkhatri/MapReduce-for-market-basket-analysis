#!/usr/bin/env python

import sys

file1 = []
file2 = []
for line in sys.stdin: 
    	
   line = line.strip()
   words = line.split('\t')
   #file with 2itemsets
   if len(words)==2:
       file1.append(line)
   #file with 3itemsets   
   else:
       file2.append(line)
     
for word in file2:
    part1,part2,part3 = word.split('\t',2)
    part = part1+'\t'+part2
    #if 3itemsets's B and C part is present in 2itemsets 
    if part  in file1:
      print('%s\t%s\t%s' % (part1,part2,part3))
    else:
      print('%s\t%s\t%s' % (part1,part2,'1')) 