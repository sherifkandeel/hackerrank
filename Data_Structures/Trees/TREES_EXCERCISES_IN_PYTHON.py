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
  

four = node()
four.data = 4 
four.left = None
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


dfs(one)











