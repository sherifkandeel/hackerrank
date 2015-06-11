import math
text = list(raw_input())
N = len(text)
c = int(math.ceil(N/math.sqrt(N)))
f = int(math.floor(N/math.sqrt(N)))
if c*f < N:
    f+=1
string = ""
for i in xrange(c):
    for j in xrange(f):
        idx = j*c + i 
        if idx < N:
            string+=text[idx]
    string+=" "
print string

