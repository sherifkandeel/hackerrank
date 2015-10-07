class node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.count = 0

    def add_child(self, n):
        self.children.append(n)

node_list = {}
n, e = map(int, raw_input().split(' '))

for i in range(e):
    v1, v2 = map(int, raw_input().split(' '))
    if v1 not in node_list:
        temp = node(v1)
        node_list[v1] = temp
    if v2 not in node_list:
        temp = node(v2)
        node_list[v2] = temp
    node_list[v2].children.append(node_list[v1])




bushes = 0
def post_order(root):
    global bushes
    if len(root.children) == 0:
        root.count = 1
    totcount = 0
    for child in root.children:
        post_order(child)
        totcount += child.count
    root.count = 1 + totcount
    if root.count %2 == 0:
        bushes +=1
        root.count = 0

post_order(node_list[1])
print bushes-1
