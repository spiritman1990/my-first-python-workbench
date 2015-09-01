#!/usr/bin/python
# Filename: continue.py

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        print "OK,It's done!"
        break
    if len(s) < 3:
        continue
    else: 
        print 'Input is of sufficient length'
