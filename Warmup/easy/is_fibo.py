fibos = []
fibos.append(0)
fibos.append(1)
fibos.append(1)
i = 3
while True:
    fibos.append(fibos[i-1] + fibos[i-2])
    if fibos[i] > 10000000000:
        break
    i+=1
fiboss = set(fibos)
T = int(raw_input())
for i in xrange(T):
    n = int(raw_input())
    if n in fiboss:
        print "IsFibo"
    else:
        print "IsNotFibo"
    
