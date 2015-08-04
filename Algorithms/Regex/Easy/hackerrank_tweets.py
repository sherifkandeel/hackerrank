import re
exp = "hackerrank"
n = int(raw_input())
count = 0
for i in range(n):
    s = raw_input()
    if re.search(exp, s, re.IGNORECASE):
        count+=1
print count
