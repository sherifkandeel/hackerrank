def  replaceBLUE(str):
    target_word = "BLUE"
    words = str.split(' ')
    resultlist = []
    for i in words: 
        if len(i) == len(target_word) and "B" in i and "L" in i and "U" in i and "E" in i:
            resultlist.append("XXXX")
        else:
            resultlist.append(i)
    return ' '.join(resultlist)


print replaceBLUE("THE PEOPLE OF REDLAND WANTS TO GET RID OF THE BLUE AND UEBL BUT LEBUS ARE GOOD") 
