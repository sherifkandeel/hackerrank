def check_substring(s1, s2):
    s1_s = ''.join(sorted(set(s1)))
    s2_s = ''.join(sorted(set(s2)))
    for c in s1_s:
        if c in s2_s:
            return "YES"
    return "NO"


cases = int(raw_input())
for i in range(0, cases):
    s1 = raw_input()
    s2 = raw_input()
    print check_substring(s1,s2)
