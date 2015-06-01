raw_input()
arr = raw_input().split(' ')

n = raw_input()
while n: 
    arr1 = n.split(" ")
    start = int(arr1[0])
    end = int(arr1[1])
    smallest = 3
    for i in xrange(start,end+1):
        if int(arr[i]) <smallest:
            smallest = int(arr[i])

    print smallest
    n = raw_input()


    

        
