n = int(raw_input())
sentences = {} #holds a dictionary with key = start letter, value = the sentence
starts = {} #holds a dictionary with key=start letter, value = end letter
ends = {}   #holds a dictionary with key=end letter, value = start letter

for i in range(n):
    s = raw_input()
    sentences[s[0]] = s
    starts[s[0]] = s[len(s)-1]
    ends[s[len(s)-1]] = s[0]



#Finding the very first sentence
startletter = ''
nextletter = ''
for k,v in starts.items():
    if k not in ends:
        startletter = k
        nextletter = v
        break


#The sorting part
sortedarray = []
sortedarray.append(sentences[startletter])
while True:
    if nextletter in sentences:
        sortedarray.append(sentences[nextletter])
    if nextletter in starts:
        nextletter = starts[nextletter]
    else:
        break

print sortedarray

#Example:
#xeng
#abdallah
#rodio
#oman
#hacker
#nix
