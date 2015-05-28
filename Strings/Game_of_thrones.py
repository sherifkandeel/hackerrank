def is_palindrome_mutation(s):
    s_set = set()
    for c in s:
        if c in s_set:
            s_set.remove(c)
        else:
            s_set.add(c)
    if len(s_set) == 0 or len(s_set) == 1:
        return True
    return False



string = raw_input()
found = False
found = is_palindrome_mutation(string)
if not found:
    print("NO")
else:
    print("YES")

