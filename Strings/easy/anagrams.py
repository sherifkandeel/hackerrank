def get_changes(s1, s2):
    s2_c = list(s2)
    for i in s1:
        if i in s2_c:
            s2_c.remove(i)
    return len(s2_c)

def anagramize(s):
    if len(s) % 2 != 0:
        return -1
    s1 = s[0:len(s)/2]
    s2 = s[len(s)/2:]
    return get_changes(s1,s2)


cases = int(raw_input())
for i in range(0, cases):
    s = raw_input()
    print anagramize(s)
