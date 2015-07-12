import random
def follow(p, s, k):
    slist = list(s)
    news = [" " for i in range(len(s))]
    for x in range(k):
        for i in range(len(s)):
            news[i] = slist[p[i]-1]
        slist = list(news)
    return news

def find_divisor(p):
    count = 0
    for i in range(len(p)):
        if p[i]-1 != i:
            count+=1
    if count ==0: return 1
    return count

def find_divisor2(p, s, k):
    slist = list(s)
    news = [" " for i in range(len(s))]
    for x in range(len(p)):
        for i in range(len(s)):
            news[i] = slist[p[i]-1]
        slist = list(news)
        if x>0 and list(news) == list(s):
            return x
    return len(p)

    
def encode(p, k, s): 
    # newk = k % find_divisor(p)
    # print newk
    return ''.join(follow(p, s, k))


print encode([1, 3, 4, 2], 5, "abcd")

for i in range(10):
    a = [i+1 for i in range(random.randint(1,50))]
    random.shuffle(a)
    p =list (a)
    random.shuffle(a)
    s = ''.join([ chr((i % 27) + 96) for i in a])
    k = random.randint(10,10000)
    print "k=%d, newk = %d, len(p)=%d"%(k,  k%find_divisor2(p, s, k), len(p),)
    print s
    str1 = encode(p, k, s)
    str2 = encode(p, k % find_divisor(p), s)
    str3 = encode(p, k % find_divisor2(p, s, k), s)
    if str1 == str3:
        print "EQUALS"
    else:
        print "NOTEQUALS"
    print "==========="
