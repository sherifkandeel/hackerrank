s = raw_input()
s = s.lower()
s_set = set()
for i in s:
    s_set.add(i)
if len(s_set) == 27 or len(s_set) == 26 and ' ' not in s_set:
    print "pangram"
else:
    print "not pangram"

