count_occurences(ls, number, index):
    total = 0
    for i in ls: 
        if i[len(i)-index] == str(number):
            total+=1
    return total
