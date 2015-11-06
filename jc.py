#!/usr/bin/python
#coding:utf8
#求n得阶乘
def N_Values(n):
    Values = 1
    for i in range(n):
        if i == 0:
            continue
        else:
            Values *= i
    return Values


print N_Values(int(input("请输入要求阶乘的数: ") + 1 ))
