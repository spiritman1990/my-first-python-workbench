#!/usr/bin/python
# coding: gbk
import os
import sys
print os.getcwd()
print "�ļ�������",sys.argv[0]
print os.path.split( os.path.realpath( sys.argv[0] ) )
FP = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
print FP