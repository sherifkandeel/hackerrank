def get_deletions(s1, s2):
    s1_c = list(s1)
    s2_c = list(s2)
    for i in s1:
        if i in s2_c:
            s1_c.remove(i)
            s2_c.remove(i)
    return len(s1_c) + len(s2_c)            


s1 = raw_input()
s2 = raw_input()
print get_deletions(s1,s2)
