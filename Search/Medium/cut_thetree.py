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

def remove_edge(nodelist,edge_string):
    a, b = map(int, edge_string.split(' '))
    nodelist[a-1].remove(nodelist[b-1])
    nodelist[b-1].remove(nodelist[a-1])


def sum_tree(root, index):
    # print root.index
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


