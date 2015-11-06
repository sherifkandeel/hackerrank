n = input()
arr = map(int, raw_input().split(' '))
arr.sort()
smallest = 10**7+1 #max limit of the problem
values = []
for i in xrange(n):
    if i == 0:
        continue
    diff = abs(arr[i] - arr[i-1])
    if smallest > diff:
        smallest = diff
        values = []
        values.append(arr[i-1])
        values.append(arr[i])
    elif smallest == diff:
        values.append(arr[i-1])
        values.append(arr[i])
        
print ' '.join(map(str, values))


