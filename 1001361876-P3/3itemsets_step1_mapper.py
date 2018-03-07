#!/usr/bin/env python

import sys

list = []
count = 0
word = None
for line in sys.stdin: 
	
   line = line.strip()
   word1, word2 = line.split('\t', 1)
   #for each word with the same first part put in the list
   if(word1==word):
       list.append(line)
   else: 
       #for the first word
       if not word:
           word = word1
           list.append(line)
           
       else:    
           word = word1
           # for each word with common first part combine it
           for i in range(0,len(list)): 
               for j in range(i+1,len(list)):
                   firstHalf1, firstHalf2 = list[i].split('\t', 1)
                   secondHalf1, secondHalf2 = list[j].split('\t', 1)
                   firstHalf1 = int(firstHalf1)
                   firstHalf2 = int(firstHalf2)
                   secondHalf2 = int(secondHalf2)
                   # to make it in ascending order
                   if (firstHalf2 < secondHalf2):
                       print('%s\t%s\t%s' % (firstHalf1,firstHalf2,secondHalf2))
                   else:
                       print('%s\t%s\t%s' % (firstHalf1,secondHalf2,firstHalf2))
           list = []
           list.append(line)
           
# for the last list         
for i in range(0,len(list)): 
   for j in range(i+1,len(list)):           
       count = count + 1
       firstHalf1, firstHalf2 = list[i].split('\t', 1)
       secondHalf1, secondHalf2 = list[j].split('\t', 1)
       firstHalf1 = int(firstHalf1)
       firstHalf2 = int(firstHalf2)
       secondHalf2 = int(secondHalf2)
       # to make it in ascending order
       if (firstHalf2 < secondHalf2):
          print('%s\t%s\t%s' % (firstHalf1,firstHalf2,secondHalf2))
       else:
          print('%s\t%s\t%s' % (firstHalf1,secondHalf2,firstHalf2))
               
       
       
       
       
       
       
       
       
         
           
   

   