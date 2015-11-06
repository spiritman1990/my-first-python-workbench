#!/usr/bin/python
# n = 15
# s = range(1, n)
# d = [s[i:i+j] for i in range(len(s)) for j in range(1, len(s)-i+1)]
# 
# print [k for k in d if sum(k) == n]


#!/usr/bin/python2


def N2S(n):
    x = n / 2 + 1 + 1
    s = [0]
    r = []
    for i in xrange(1, x): s.append(s[-1] + i)

    for i in xrange(1, x):
        for j in xrange(i + 1, x):
            v = s[j] - s[i - 1]
            if v > n: break
            if v == n:
                r.append(xrange(i, j + 1))
                break
                
    for i in r: print list(i)

N2S(200000)