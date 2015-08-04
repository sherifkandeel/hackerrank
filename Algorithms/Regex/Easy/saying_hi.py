import re
exp = "^[hH][iI]\s(?![dD]).*"
n = int(raw_input())
for i in range(n):
    s = raw_input()
    if re.search(exp, s):
        print s
