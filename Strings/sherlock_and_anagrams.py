import math
def get_pairs_count(s):
    instances = {}
    for ws in range(1, len(s)+1): #ws: window size
        for i in range(0, len(s)+1-ws):
            ss = ''.join(sorted(s[i:i+ws]))
            if ss in instances:
                instances[ss]+=1
            else:
                instances[ss] = 1 
    pairs = 0                    
    for k,v in instances.items():
        if v >= 2:
            pairs += math.factorial(v)/(math.factorial(v-2)*2) #permutations without repitions nor order
    return pairs


cases = int(raw_input())
for i in range(0, cases):
    print get_pairs_count(raw_input())
