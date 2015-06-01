def valid_pair(s1,s2,mm):
    mismatch = 0
    for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                mismatch+=1
                if mismatch > mm:
                    return False
    return True

def valid_pair_in_list(l1,l2,mm):
    for s1 in l1:
        for s2 in l2: 
            if valid_pair(s1, s2, mm):
                return True


def get_longest_substring(s1, s2, mm):
    longest_substring = 0
    for ws in range(1, len(s1)+1):
        l1 = []
        l2 = []
        for i in range(0, len(s1)+1-ws):
            l1.append(s1[i:i+ws])
            l2.append(s2[i:i+ws])
        if valid_pair_in_list(l1, l2, mm) and ws> longest_substring:
            longest_substring = ws
    return longest_substring


cases = int(raw_input())
for i in xrange(cases):
    mm, s1, s2 = raw_input().split(' ')
    mm = int(mm)
    print get_longest_substring(s1,s2,mm)
