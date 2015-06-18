import re
exp = "^[a-z]?[a-z]?[a-z]?[0-9][0-9][0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[A-Z][A-Z][A-Z]+$"
n = int(raw_input())
for i in range(n):
    s = raw_input()
    if re.search(exp, s):
        print "VALID"
    else:
        print "INVALID"
