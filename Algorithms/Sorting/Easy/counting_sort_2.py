n = int(raw_input())
arr = map(int, raw_input().split(' '))
count = [0 for i in xrange(100)]

for i in arr:
    count[i] +=1

sorted = []
for i in xrange(len(count)):
    for j in range(count[i]):
        sorted.append(i)

print ' '.join(map(str, sorted))
