#!/usr/bin/env python

import sys
import re

for line in sys.stdin: 
	
   line = line.strip()
   words = re.findall(r"[\'A-Za-z0-9]+", line)

   # for each word in list pair it with the others.
   for i in range(0,len(words)): 
     for j in range(i+1,len(words)):
       print('%s\t%s\t%s' % (words[i],words[j],1))