import math

def is_funny(s, r):
    for i in range(1,len(s)):
        s_diff = math.fabs(ord(s[i]) - ord(s[i-1]))
        r_diff = math.fabs(ord(r[i]) - ord(r[i-1]))
        if s_diff != r_diff: 
            return False
    return True

cases = int(raw_input())
for c in range (0, cases):
    s = raw_input()
    r = s[::-1]
    funny = is_funny(s, r)
    if funny:
        print "Funny"
    else:
        print "Not Funny"


