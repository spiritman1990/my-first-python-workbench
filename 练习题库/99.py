#!/usr/bin/python
#coding:utf8
#输入一个正数n，输出所有和为n连续正数序列
#例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3个连续序列1-5、4-6和7-8。
import math
def calc(n):
    h = int(math.sqrt(2*n))
    for k in range(2,h+1):
        if((2*n) % k == 0):
            t1 = 2 * n - k*k + k
            t2 = 2 * n + k*k - k
            #print t1,t2
        if t1 % (2*k) == 0 and t2 % (2*k) == 0:
            s1 = t1 / (2*k)
            s2 = t2 / (2*k)
            print s1,"-",s2
#             for i in range(s1,s2+1):
#                 print i,
calc(18)                    
                    
    