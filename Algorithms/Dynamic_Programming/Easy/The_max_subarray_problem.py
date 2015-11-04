def max_contiguous(arr):
    best_sum = max(arr)
    if best_sum < 0:
        return best_sum
    current_sum = 0
    for i in range(len(arr)):
        if current_sum < 0:
            current_sum = 0 
        if arr[i] + current_sum < current_sum:
            if current_sum > best_sum:
                best_sum = current_sum
        current_sum += arr[i]
    return max(best_sum, current_sum)

def max_non_contiguous(arr):
    if max(arr) < 0:
        return max(arr)
    best_sum = 0
    for i in range(len(arr)):
        if best_sum + arr[i] > best_sum:
            best_sum+=arr[i]
    return best_sum

        
t = input()
for i in range(t):
    input()
    arr = map(int, raw_input().split(' '))
    print "%d %d"%(max_contiguous(arr),max_non_contiguous(arr))
    
            
        
