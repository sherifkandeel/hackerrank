import Queue
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_emtpy(self):
        return self.items == []

class node:
    data = 0
    left = None
    right = None
  

six = node()
six.data = 6
six.left = None
six.right = None

four = node()
four.data = 4 
four.left = six
four.right = None

five = node()
five.data = 5
five.left = None
five.right = None

two = node()
two.data = 2
two.left = None
two.right = four

three = node()
three.data = 3
three.left = None
three.right = five


one = node()
one.data = 1
one.left = two
one.right = three


def depth(node):
    if node == None:
        return 0 
    d1 = depth(node.left) + 1 
    d2 = depth(node.right) + 1
    return max(d1, d2)
    
# print depth(one)    

# deepest = 0
# value = 0
# def deepest_node(node, depth):
#     global deepest
#     global value
#     if node == None:
#         return
#     if node.left == None and node.right == None:
#         if depth > deepest:
#             value = node.data
#             deepest = depth
#         return
#     deepest_node(node.left, depth+1)
#     deepest_node(node.right, depth+1)


def deepest_node(node, depth, deepestvalue):
    if node == None:
        return depth, deepestvalue
    d1, v1 = deepest_node(node.left, depth+1, node.data)
    d2, v2= deepest_node(node.right, depth+1, node.data)
    if d1 > d2:
        return d1, v1
    else:
        return d2, v2
    

# deepest, value = deepest_node(one, 0, 0)
# deepest_node(one, 1)
# print deepest, value


def deepest_path(node, depth, deepestpath):
    if node == None:
        return depth, deepestpath
    d1, v1 = deepest_path(node.left, depth+1, deepestpath+" "+str(node.data))
    d2, v2= deepest_path(node.right, depth+1, deepestpath+" "+str(node.data))
    if d1 > d2:
        return d1, v1
    else:
        return d2, v2
    
d, st = deepest_path(one, 0, "")
print d, st



def post_order_traverse(node):
    if node == None:
        return
    post_order_traverse(node.left)
    post_order_traverse(node.right)
    print node.data

# post_order_traverse(one)


def pre_order_traverse(node):
    if node == None:
        return
    print node.data
    pre_order_traverse(node.left)
    pre_order_traverse(node.right)
# pre_order_traverse(one)


def in_order_traverse(node):
    if node == None:
        return
    in_order_traverse(node.left)
    print node.data
    in_order_traverse(node.right)

# in_order_traverse(one)


def bfs(node):
    q = Queue.Queue()
    q.put(node)
    while not q.empty():
        n = q.get()
        if n.left:
            q.put(n.left)
        if n.right:
            q.put(n.right)
        print n.data

# bfs(one)


def dfs(node):
    s = Stack()
    s.push(node)
    n = node
    while not s.is_emtpy():
        n = s.pop()
        if n.right:
            s.push(n.right)

        if n.left:
            s.push(n.left)
        print n.data


# dfs(one)











