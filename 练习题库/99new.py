#!/usr/bin/python
#coding:utf8
def NumberSequence(number):
    base = 2
    while (number - base * (base + 1) / 2) >= 0 :
        if (number - base * (base + 1) / 2) % base == 0:
            start = (number - base * (base + 1) / 2) / base
            print range(start + 1, start + base + 1)
        base += 1
NumberSequence(20000000000)        