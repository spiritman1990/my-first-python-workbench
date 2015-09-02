#!/usr/bin/python
import random
j = random.randint(1,10) 

i = 0
s=""
while (i < 4):
    if (j >> i & 1):
        s = '1' + s
    else:
        s = '0' + s 
    i = i + 1
print ("%d : 0000%s" %(j,s))    

00000100 & 00000001