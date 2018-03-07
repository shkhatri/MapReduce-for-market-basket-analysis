#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	
     line = line.strip()
     word1,word2,word3,count = line.split('\t', 3)
     word=word1+'\t'+word2+'\t'+word3
     try:
           count = int(count)
     except ValueError:
	      continue

     if current_word == word:
	     current_count += count
     else:
          #count the number of times the 3itemsets appear in transaction table
          if current_word:
              #if the number is greater than 1000 it is frequent
              if(current_count>1000):
                    part1,part2,part3 = current_word.split('\t', 2)
                    print('%s\t%s\t%s' % (part1,part2,part3))
          current_count = count
          current_word = word

if current_word == word:
    if(current_count>1000):
       part1,part2,part3 = current_word.split('\t', 2)
       print('%s\t%s\t%s' % (part1,part2,part3))
    