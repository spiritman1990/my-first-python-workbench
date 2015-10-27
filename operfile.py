#!/usr/bin/python
#coding:gbk
import os
# to operate the files, such as create,write,read,delete and append
# write a file for test
phrases='''2015年10月27日17:20:51
今天状态不好啊
精神不振
晚上还要去健身房
真他妈的累啊
提防小人啊
'''
DIR = os.getcwd() 
OLDF = open("%s/oper1.txt"%(DIR),"w")
OLDF.close()
w=file("%s/oper.txt"%(DIR),"w+")
w.write(phrases)
w.close
h=file("%s/oper.txt"%(DIR),"a+")
h.write(phrases)
h.close()
#read from a file that already exists
k=file("%s/oper.txt"%(DIR),"r")
for s in k.readlines():
    print s
k.close()  
#to delete a a file that exists
if os.path.isfile("%s/oper1.txt"%(DIR)):
    os.remove("%s/oper1.txt"%(DIR))
    print "删除成功"
else:
    print "文件不存在，无法删除"    