def count_occurences(ls, number, index):
    total = 0
    for i in ls: 
        if len(i)-index >= 0 and i[len(i)-index] == str(number):
            total+=1
    return total

#that's for generating the permutations themselves, it times out of course when doing the total
l4t, l5t, l6t = map(int, raw_input().split(' '))
MOD = 10**9 + 7
ls = []
total =0
def F(l4, l5, l6, number):
    global ls
    global total
    if l4<=l4t:
        ls.append(str(number*10 + 4))
        total = (total + number*10 + 4) % MOD
        F(l4+1, l5, l6, (number*10 + 4) % MOD)

    if l5<=l5t:
        ls.append(str(number*10 + 5))
        total = (total + number * 10 + 5) % MOD
        F(l4, l5+1, l6, (number * 10 + 5) % MOD)

    if l6<=l6t:
        ls.append(str(number*10 + 6))
        total = (total + number *10 + 6) % MOD
        F(l4, l5, l6+1, (number * 10 + 6) % MOD)


F(1, 1, 1, 0)
print total % MOD


print "FOURS: "
for i in range(l4t+l5t+l6t):
    print "%d >> %d"%(10**(i+1),count_occurences(ls, 4, i+1))

print "FIVES: "
for i in range(l4t+l5t+l6t):
    print "%d >> %d"%(10**(i+1),count_occurences(ls, 5, i+1))

print "Sixes: "
for i in range(l4t+l5t+l6t):
    print "%d >> %d"%(10**(i+1),count_occurences(ls, 6, i+1))



#def get_ones(r, n):
#    return 1+ r*(2*(n-1))
#
#def get_tens(r, n):
#    return r*(2*(n-1))
#
#def get_hundreds(r, n):
#    return r*(n-1)
#
#l4t, l5t, l6t = map(int, raw_input().split(' '))
#MOD = 10**9 + 7
#total =0
#
#if (l4t == 0 and l5t > 0 and l6t > 0) or (l5t == 0 and l4t > 0 and l6t > 0) or (l6t == 0 and l4t > 0 and l5t > 0): 
#    n = 2
#
#elif (l4t == 0 and l5t == 0 and l6t > 0) or (l4t == 0 and l6t == 0 and l5t > 0) or (l6t == 0 and l5t == 0 and l4t > 0): 
#    n = 1
#
#elif l4t == 0 and l5t == 0 and l6t == 0:
#    n = 0
#
#else:
#    n = 3
#
#if n > 0:
#    total += 4 * get_ones(l4t, n) + 40 * get_tens(l4t, n) + 400 * get_hundreds(l4t, n)
#    total += 5 * get_ones(l5t, n) + 50 * get_tens(l5t, n) + 500 * get_hundreds(l5t, n)
#    total += 6 * get_ones(l6t, n) + 60 * get_tens(l6t, n) + 600 * get_hundreds(l6t, n)
#print total




