import re
exp = "([0-9]+)[-\s]([0-9]+)[-\s]([0-9]+)"
n = int(raw_input())
for i in range(n):
    s = raw_input()
    matches = re.match(exp, s)
    print "CountryCode=%s,LocalAreaCode=%s,Number=%s"%(matches.group(1),matches.group(2),matches.group(3))
