#not solved yet!
def isprime (num):
    if num <=1 :
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num*0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

t = input()
for i in range(t):
    case = input()
    if case < 4:
        print 0
        continue
    case -= 2
    primes = 0
    for i in range(case+1):
        if isprime(i): 
            primes += 1
    print "-----"
    print primes
    print "-----"
        
