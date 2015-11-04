# It does exceed the time limit because it is o(n2) and there's also a dp solution that does it in o(nlogn)
# I don't know yet how to implement that one
n = input()
arr = []
for i in range(n):
    arr.append(input())
dp = [1 for x in range(n)]
for i in range(1,n):
    maxx = 0
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] > maxx: 
                maxx = dp[j]
    dp[i] = maxx+1
print max(dp)
    
        
    
