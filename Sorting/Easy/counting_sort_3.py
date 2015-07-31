n = int(raw_input())
arr = []
for i in range(n):
    arr.append(int(raw_input().split(' ')[0]))

count = [0 for i in range(100)]
for i in arr:
    count[i] += 1
    
sorted = [0 for i in range(100)]
sorted[0] = count[0]
for i in range(1,len(sorted)):
    sorted[i] = sorted[i-1] + count[i]

print ' '.join(map(str, sorted))
