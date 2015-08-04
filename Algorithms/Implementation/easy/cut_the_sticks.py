
def get_smallest(n):
    if not n: return -1
    smallest = n[0]
    for i in n:
        if i<smallest:
            smallest = i
    return smallest


def cut(n):
    c = get_smallest(n)
    m = []
    for i in n:
        i -=c
        if i>0:
            m.append(i)
    return m   

raw_input()
n = raw_input().split(' ')
m = []
for i in n:
    m.append(int(i))

while len(m) > 0:
    print len(m)
    m = cut(m)
