def get_palindrome_breakingpoint(s):
    for i in range(0, len(s)):
        if s[i] != s[len(s)-1-i]:
            return i
    return -1


def remove_char(s,i):
    if i== len(s)-1:
        return s[:-1]
    return s[:i] + s[i+1:]


def get_index(s):
    idx = get_palindrome_breakingpoint(s)
    sn1 = remove_char(s,idx)
    sn2 = remove_char(s,len(s)-1-idx)

    if get_palindrome_breakingpoint(sn1) == -1:
        return idx
    return len(s)-1-idx


cases = int(raw_input())
for i in range(0, cases):
    print get_index(raw_input())
