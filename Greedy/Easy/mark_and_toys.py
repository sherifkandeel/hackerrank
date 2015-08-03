n, k = map(int, raw_input().split(' '))
arr = map (int, raw_input().split(' '))
arr.sort()
sum = 0
for i in range(n):
    sum += arr[i]
    if sum > k:
        print i
        break

