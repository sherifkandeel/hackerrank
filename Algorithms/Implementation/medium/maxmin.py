N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort() #this guarantees that the min is the first of the k-subsequence and the max is the last of the subsequence, and sorting in python is o(nlogn)
min_diff = -1
for i in xrange(N+1-K):
    maximum = lists[i+K-1]
    minimum = lists[i]
    if maximum - minimum < min_diff or min_diff == -1:
        min_diff = maximum-minimum
print min_diff
