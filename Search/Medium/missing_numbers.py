n = int(raw_input())
a = map(int, raw_input().split(' '))
ad = {}
for i in a:
    if i in ad:
        ad[i] += 1
    else:
        ad[i] = 1
m = int(raw_input())
b = map(int, raw_input().split(' '))
bd = {}
for i in b:
    if i in bd:
        bd[i] += 1
    else:
        bd[i] = 1

missing = set()
for k,v in ad.items():
    if k in bd:
        if v != bd[k]:
            missing.add(k)
sl = list(missing)
sl.sort()
print ' '.join(map(str,sl))


