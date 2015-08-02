#NOT SOLVED YET!
#Apparently we need something more powerful than a prefix tree. or maybe a sorted one? 

def getprefixarr(arr, n, m):
    curr = 0
    prefix = []
    for i in range(n):
        curr = (arr[i] % m + curr)%m
        prefix.append(curr)
    return prefix




def solve(n, m, arr):
    prefix = getprefixarr(arr, n, m)
    ret = 0
    for i in range(n):
        for j in range(i-1,-1,-1):
            ret = max(ret, (prefix[i] - prefix[j] + m) % m)
        ret = max(ret, prefix[i])
    return ret



t = int(raw_input())
for i in xrange(t):
    n, m = map(int, raw_input().split(' '))
    arr = map(int, raw_input().split(' '))
    print solve(n, m, arr)


# n = 5
# m = 7
# arr = [3, 3, 9, 9, 5]
# print solve(n, m, arr)

# def solve(n, m, arr):
#     maxsum = 0
#     newarr = []
#     for i in xrange(n):
#         for j in xrange(len(arr)-1):
#             tempsum = (arr[j]+arr[j+1])
#             newarr.append(tempsum)
#             if (tempsum % m) > maxsum:
#                 maxsum = tempsum
#         arr = list(newarr)
#         newarr = []
#     return maxsum

# def solve(n, m, arr):
#     max_sum = 0
#     sub_sum = 0
#     for ws in xrange(n):
#         for i in xrange(n-ws):
#             if i ==0:
#                 sub_sum = sum(arr[i:i+ws])
#             else:
#                 sub_sum = sub_sum-arr[i-1]+arr[i+ws-1]
#             if sub_sum%m > max_sum:
#                 max_sum = sub_sum
#     return max_sum

# class node:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, obj):
#         self.children.append(obj)



# def solve(n, m, arr):
#     nodes = []
#     for i in xrange(n):
#         nodes.append(node(arr[i]))
    

# def create_tree(root, n, lvl):
#     if lvl > n: 
#         return
#     root.add_child(node(lvl))
#     root.add_child(node(lvl))
#     for child in root.children:
#         create_tree(child, n, lvl+1)



# def traverse_tree(root):
#     print root.value
#     for child in root.children:
#         traverse_tree(child)
    
