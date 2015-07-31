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



