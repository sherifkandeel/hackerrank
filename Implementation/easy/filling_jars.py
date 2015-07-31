n, m = map(int, raw_input().split(' '))
total =0
for i in xrange(m):
    a,b,k = map(int, raw_input().split(' '))
    total += (b-a+1)*k

print total/n



