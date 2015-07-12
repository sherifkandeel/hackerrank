#One thing that makes this pretty straight forward is this: (n+1)^2−n^2=2n+1 Start with one, and keep on adding that.
#This is also a valid solution to count the ints between the square roots of the limits
import math
T = int(raw_input())
for i in xrange(T):
    l,u = map(int, raw_input().split(' '))
    count = 0
    ls = int(math.sqrt(l))
    us = int(math.sqrt(u))
    for i in xrange(ls,us):
        count +=1
    if ls*ls ==l:
        count+=1
    print count

