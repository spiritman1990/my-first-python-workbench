#!/usr/bin/python
# to combine the source string with my way,such as C3 stands for CCC
import re
STR='''
(AA)2A
((A2B)2)2G
WANGYI
A2BC4D2
'''
F1=file("arrtst.txt","w+")
F1.write(STR)
F1.close()
F2=file("arrtst.txt","r+")
for k in F2.readlines():
    n = re.match(r'\((.*)\)(.*)', k)
    if n:
        #print n.group()
        print n.group(1),n.group(2)