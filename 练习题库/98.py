#!/usr/bin/python
#coding:utf8
#求1+2+…+n
n = raw_input("请输入一个大于1的正整数:")
while not n.isdigit():
    print "输入的内容不符合要求，请重新输入!"
    n = raw_input("请输入一个大于1的正整数:")
else:
    n = int(n)    
def s(x,y):
    return x+y
print "开始计算1..%d的和"%(n)
print reduce(s,range(1,n+1))