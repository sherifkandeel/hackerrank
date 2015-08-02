n, k = map(int, raw_input().split(' '))
arr = map(int, raw_input().split(' '))
setarr = set(arr)

total = 0
for num in arr:
    if num-k != num and (num-k) in setarr:
        total+=1
print total



