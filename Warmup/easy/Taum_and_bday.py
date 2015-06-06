T = int(raw_input())
for i in xrange(T):
    b, w = map(int, raw_input().split(' '))
    x, y, z = map(int, raw_input().split(' '))
    cost = 0
    if b*x > (b*y + b*z):
        cost = b*y + b*z + w*y
    elif w*y > (w*x + w*z):
        cost = w*x + w*z + b*x
    else:
        cost = b*x + w*y
    print cost

