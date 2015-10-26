#!/bin/python
# coding: gbk
# make by paul
# why can not send to my git hub ???
import time
num = raw_input("请输入一个整数:")
while not num.isdigit():
    num = raw_input("请重新输入一个正整数:")
else:
    num = int(num)
print "输入的数字是",num
print "开始求",num,"的二进制表示方法:"
s='.'
for c in range(1,10):
    d = c * 10
    time.sleep(0.5)
    print "计算进度：%d%% [ " % d + s*c +" ]","\n"
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
print "结果是:",res    
    