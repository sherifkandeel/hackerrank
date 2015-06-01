#def solution(A): total = 0
#    for i in A:
#        total +=i
#        
#    left = total
#    so_far = 0
#    for i in xrange(len(A)):
#        left = left - A[i]
#        if left == so_far:
#            return i
#        so_far +=A[i]
#    return -1
#
#
#A = [-1,3,-4,5,1,-6,2,1]
#print solution(A)

l = [1,2,3,4,6]
print max(l[2:3])
print 
