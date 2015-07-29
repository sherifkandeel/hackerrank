class node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


n = int(raw_input()) 
values = map(int, raw_input().split(' '))

edges = {}
for i in range(n-1):
    k,v = map(int, raw_input().split(' '))
    if k in edges:
        edges[k].append(v)
    else:
        edges[k] = [v] 
print edges


root = node(0)
child1 = node(1)
child2 = node(2)
child3 = node(3)
child4 = node(4)
child1.add_child(child3)
child1.add_child(child4)
root.add_child(child1)
root.add_child(child2)


def traverse(root):
    if not root:
        return
    print root.value
    for c in root.children:
        traverse(c)
    return

traverse(root)



# def traverse(root, index):
#     print root.index
#     raw_input()
#     for c in root.connections:
#         if c.index == index:
#             print "skipping"
#         else:
#             traverse(c, root.index)
#     return
#traverse(nodes[0], 0)



#Traverse check
# for node in nodes:
#     for connection in node.connections:
#         print "%d - > %d" %(node.index, connection.index)

# for node in nodes:
#     print "%d: %d"%(node.index, node.summation)

import random 
class node:
    def __init__(self, value, index):
        self.index = index
        self.value = value
        self.connections = []
        self.summation  = 0

    def add_connection(self, obj):
        self.connections.append(obj)

    def remove_connection(self, obj):
        if obj in self.connections:
            self.connections.remove(obj)
        
    def add_sum(self, summation):
        self.summation = summation



count = int(raw_input())
values = map(int, raw_input().split(' '))
nodes = []
edges = []
for i in range(count):
    nodes.append(node(values[i], i))

for i in range(count-1):
    inp = raw_input()
    edges.append(inp)
    a, b = map(int, inp.split(' '))
    nodes[a-1].add_connection(nodes[b-1])
    nodes[b-1].add_connection(nodes[a-1])


def sum_tree(root, index):
    summ = root.value
    for c in root.connections:
        if c.index != index:
           summ += sum_tree(c, root.index)
    root.summation = summ
    return summ


sum_tree(nodes[0], 0)
treesum = nodes[0].summation #Treesum lol
minimum = 9999999
def get_minimum(root, index):
    global minimum
    for c in root.connections:
        if c.index != index:
            # print "at node %d, %d, %d, %d"%(c.index, treesum, root.summation, c.summation)
            difference = abs(treesum - c.summation)
            difference = abs(c.summation - difference)
            if difference < minimum:
                minimum = difference
            get_minimum(c, root.index)


get_minimum(nodes[0], 0)
print minimum



def generate_nodes(num):
    nodearray  = []
    for i in range(num):
        nodearray.append(random.randint(1, 1001))
    return nodearray

def generate_edges(num):
    edgearray = []
    for i in range(num-1):
        edgearray.append("%d %d"%(rnadom.randint(1, num), rnadom.randint(1, num)))
    return edgearray








