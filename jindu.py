#!/usr/bin/python
# coding: UTF-8

import time

s="#"
b="\b"

print "软件 1 开始安装..... \n"
for x in range(1,101):
    time.sleep(0.1)
    print b* 150 + "进度：%d%% [ " % x + s*x +" ]","\n",
print "\n1 安装结束..."