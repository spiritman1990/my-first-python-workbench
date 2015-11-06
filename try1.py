#!/usr/bin/python
#coding:utf8
import os
try:
    DIR="c:\python"
    os.chdir(DIR)
    os.getcwd()
except  WindowsError:
    print "Faild to change directory %s"%(DIR)
else:
    print "当前目录是%s"%DIR
finally:
    print "我总算是彻底对这垃圾烂公司看透了"