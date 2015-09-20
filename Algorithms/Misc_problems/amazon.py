def get_distance(w1, w2):
    w1list = list(w1)
    w2list = list(w2)
    distance = 0
    for i in range(len(w1list)):
        if w1list[i] != w2list[i]:
            distance +=1
    return distance
    
    
def solve(start, end, worddict):
    newstart = start        
    initial_diff = get_distance(newstart, end)
    print newstart
    while initial_diff > 1: 
        valid_words = []       
        for word in worddict:
            if get_distance(newstart, word) == 1:
                 valid_words.append(word)
      
        if len(valid_words) == 0:
            return False
        
        mindifference = 999 #or max distance according to the input limits
        mindiffword = ""            
        for word in valid_words:
            if get_distance(word, end) < mindifference:
                mindifference = get_distance(word, end)
                mindiffword = word
        newstart = mindiffword
        print newstart
        worddict.remove(newstart)
        initial_diff = mindifference
    return True
            
start = "hit"
end = "cog"
worddict = ["hot","dot","dog","lot","log"]
print solve(start, end, worddict)

#  "hit" -> "hot" -> "dot" -> "dog" -> "cog"
1
