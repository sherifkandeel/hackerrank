import operator
n = int(raw_input())
start=[]
end=[]
times = {}
for i in range(n):
    s, e = map(int, raw_input().split(' '))
    start.append(s)
    end.append(e)
    times[i+1] = s+e

times_sorted = sorted(times.items(), key=operator.itemgetter(1))
sortedtimeslist = []
[sortedtimeslist.append(str(k)) for k,v in times_sorted]
print ' '.join(sortedtimeslist)


