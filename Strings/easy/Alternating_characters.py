def get_number_of_deletions(s):
    deletions = 0
    for c in range(1,len(s)):
        if s[c] == s[c-1]:
            deletions +=1
    return deletions

cases = int(raw_input())
for i in range(0,cases):
    s =  raw_input()
    d = get_number_of_deletions(s)
    print d
