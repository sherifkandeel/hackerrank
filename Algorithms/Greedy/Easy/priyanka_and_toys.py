n  = int(raw_input())
weights = map(int, raw_input().split(' '))
weights.sort()
weight_limit = -1 
bought = 0 
for w in weights:
    if w > weight_limit:
        bought +=1 
        weight_limit = w+4
print bought
