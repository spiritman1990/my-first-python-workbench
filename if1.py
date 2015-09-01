#!/usr/bin/python
#coding:utf-8
num = 10
num2 = int(raw_input('请输入一个整数：'))

if num <  num2:
    print "你输入的数比num大"
    print 'Done'
elif num > num2:
    print "你输入的数字比num小"
else:
    print "一样大"