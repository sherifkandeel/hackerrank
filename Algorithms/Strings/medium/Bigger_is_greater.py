def rearrange(s):
    s_r = list(s[::-1])
    for i in range(0,len(s_r)):
        for j in range(0,i):
            if s_r[j]>s_r[i]:
                temp = s_r[i]
                s_r[i] = s_r[j]
                s_r[j] = temp
                s_r[0:i] = sorted(s_r[0:i])[::-1]
                return ''.join(s_r[::-1])
    return "no answer"
                
cases = int(raw_input())
for i in range(0,cases):
    s = raw_input()
    print rearrange(s)

