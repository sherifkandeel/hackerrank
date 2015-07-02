cases = int(raw_input())
for i in range(cases):
    m = int(raw_input())
    n = int(raw_input())
    arr = map(int, raw_input().split(' '))
    values = {}
    count = 0
    for i in arr:
        values[i] = count
        count += 1
    for i in range(len(arr)): 
        if m-arr[i] in values and values[m-arr[i]] > i: 
            print i+1, values[m-arr[i]]+1
            break
             
