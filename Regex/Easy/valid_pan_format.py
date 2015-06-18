import re
exp = "[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]"
n = int(raw_input())
for i in range(n):
    s = raw_input()
    if re.search(exp, s):
        print "YES"
    else:
        print "NO"
