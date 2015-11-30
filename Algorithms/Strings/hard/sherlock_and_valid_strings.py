s = list(raw_input())
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
vals = dic.values()
valsdic = {}
for i in vals:
    if i in valsdic:
        valsdic[i] +=1
    else:
        valsdic[i] = 1

#print valsdic
if len(valsdic.keys()) > 2:
    print "NO"
elif len(valsdic.keys()) == 2:
    if abs(valsdic.keys()[0] - valsdic.keys()[1]) > 1 and (valsdic[valsdic.keys()[0]] == 1 or valsdic[valsdic.keys()[1]] == 1):
        print "YES"      
    elif abs(valsdic.keys()[0] - valsdic.keys()[1]) > 1 or (valsdic[valsdic.keys()[0]] != 1 and valsdic[valsdic.keys()[1]] != 1):
        print "NO"    
    else:
        print "YES"
else:
    print "YES"



