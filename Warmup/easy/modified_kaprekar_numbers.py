def is_kaprekar(n):
    m = str(n*n)
    l = m[0:len(m)/2]
    r = m[len(m)/2:]
    if len(l)==0:
        l="0"
    if int(l) + int(r) == n:
        return True
    return False


p = int(raw_input())
q = int(raw_input())
kaprekars = []
for i in range(p,q+1):
    if is_kaprekar(i):
        kaprekars.append(i)
if len(kaprekars) == 0:
    print "INVALID RANGE"
else:
    print ' '.join(map(str,kaprekars))
