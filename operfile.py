#!/usr/bin/python
#coding:gbk
import os
# to operate the files, such as create,write,read,delete and append
# write a file for test
phrases='''2015��10��27��17:20:51
����״̬���ð�
������
���ϻ�Ҫȥ����
��������۰�
���С�˰�
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
    print "ɾ���ɹ�"
else:
    print "�ļ������ڣ��޷�ɾ��"    