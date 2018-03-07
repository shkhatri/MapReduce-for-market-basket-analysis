#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	
     line = line.strip()
     word1,word2, count = line.split('\t', 2)
     word=word1+'\t'+word2
     
     try:
           count = int(count)
     except ValueError:
	      continue
     # if first word is same as remaining words then increase counter
     if current_word == word:
	     current_count += count
     else:
         # first word not matching the word then check the count and print it
          if current_word:
              if(current_count>1000):
                    print('%s' % (current_word))
          current_count = count
          current_word = word

if current_word == word:
    if(current_count>1000):
       print('%s' % (current_word))