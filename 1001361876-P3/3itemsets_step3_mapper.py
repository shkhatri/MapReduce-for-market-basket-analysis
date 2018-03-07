#!/usr/bin/env python

import sys
words = []
ListCand = []
candidates = open('candidates', 'r')

for entry in sys.stdin: 
   ListCand.append(entry)
        
for line in candidates:    	
   line = line.strip()
   part1,part2,part3 = line.split('\t',2)
   i = 0
   words = []
   # print the no. of times the 3itemsets appear in trasaction table
   for i in range(0,len(ListCand)):
      entry = ListCand[i].strip()
      words = entry.split(' ')
      if(part1 in words and part2 in words and part3 in words):  
         print('%s\t%s\t%s\t%s' % (part1,part2,part3,'1'))  
   
     