import re
startswith = "^hackerrank.*$"
endswith = ".*hackerrank$"

n = int(raw_input())
for i in range(n):
    s = raw_input()
    if re.search(startswith, s):
        if re.search(endswith, s):
            print 0
        else:
            print 1
    elif re.search(endswith, s):
        print 2
    else:
        print -1

