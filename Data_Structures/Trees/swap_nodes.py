import Queue, sys, resource
class node:
    data = 0
    left = None
    right = None

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

n = int(raw_input())
nodes = []
for i in range(n):
    temp = node()
    temp.data = i+1
    nodes.append(temp)
  
for i in range(n):
    l, r = map(int, raw_input().split(' '))
    if l > 0:
        nodes[i].left = nodes[l-1]
    if r > 0:
        nodes[i].right = nodes[r-1]


def swap(node, lvl, threshold):
    if node == None:
        return
    if lvl == threshold:
        temp = node.left
        node.left = node.right
        node.right = temp
        return
    swap(node.left, lvl+1, threshold)
    swap(node.right, lvl+1, threshold)

def depth(node, lvl):
    if node == None:
        return lvl
    l1 = depth(node.left, lvl+1)
    l2 = depth(node.right, lvl+1)
    return max(l1, l2)


def bfs(node):
    q = Queue.Queue()
    q.put(node)
    while not q.empty():
        n = q.get()
        print n.data
        if n.left:
            q.put(n.left)
        if n.right:
            q.put(n.right)

def inorder(node, valuesofar):
    if node == None:
        return ""
    valuesofar = inorder(node.left, valuesofar)
    valuesofar += str(node.data)+" "
    valuesofar += inorder(node.right, valuesofar)
    return valuesofar

# def inorder(node):
#     if node == None:
#         return
#     inorder(node.left)
#     print node.data
#     inorder(node.right)


t = int(raw_input())
for i in range(t):
    threshold = int(raw_input())
    tree_depth = depth(nodes[0], 0)
    while threshold < tree_depth:
        swap(nodes[0], 1, threshold)
        threshold += threshold 
    print inorder(nodes[0], "")
