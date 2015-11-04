a, b, n = map(int, raw_input().split(' '))
i = 2
while i < n:
    t = b
    b = a + b*b
    a = t
    i+=1
print b
