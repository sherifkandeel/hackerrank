n, k = map(int, raw_input().split(' '))
permutations = map(int, raw_input().split(' '))
index = {}
for i in range(n):
    index[permutations[i]] = i

for i in range(n):
    if k ==0:
        break
    if permutations[i] == n-i:
        continue
    temp = permutations[i]
    permutations[i] = n-i
    permutations[index[n-i]] = temp
    m = index[n-i]
    index[n-i] = i
    index[temp] = m
    k-=1


print ' '.join(map(str, permutations))
