pi = "31415926535897932384626433833"
T = int(raw_input())
def solve(words):
    for j in xrange(len(words)):
        if len(words[j]) != int(pi[j]):
            return "It's not a pi song."
    return "It's a pi song."

for i in xrange(T):
    words = raw_input().split(' ')    
    print solve(words)



