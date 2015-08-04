n = int(raw_input())
arr = map(int, raw_input().split(' '))
count = [0 for i in xrange(100)]

for i in arr:
    count[i] +=1


print ' '.join(map(str, count))
