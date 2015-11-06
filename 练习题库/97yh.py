#!/usr/bin/python
#coding:utf8
#2015年9月7号，题目：在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b。
D=list('abaccdeff')
E={}
F=[]
for i in D:
    if E.get(i):
        E[i]+=1
    else:
        E[i]=1
for k in E:
    for g in range(0,len(D)):
        if E[k] == 1 and D[g] == k:
            F.append(g)
print D[min(F)]     