#!/bin/python
# coding: gbk
# make by paul
# why can not send to my git hub ???
import time
num = raw_input("������һ������:")
while not num.isdigit():
    num = raw_input("����������һ��������:")
else:
    num = int(num)
print "�����������",num
print "��ʼ��",num,"�Ķ����Ʊ�ʾ����:"
s='.'
for c in range(1,10):
    d = c * 10
    time.sleep(0.5)
    print "������ȣ�%d%% [ " % d + s*c +" ]","\n"
res = ""
 
while (num-1)/2 >=0:
    if num%2:
        res = res+"1"
        num = (num-1)/2 
    elif not num%2:
        res = res+"0"
        num = num/2        
if len(res) < 8:
    res = '0'*(8-len(res))+res
else:
    res = res
print "�����:",res    
    