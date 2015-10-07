class node(object):
    def __init__(self, data):
        self.data = data
        self.connections = []
        self.weights = []

t = int(raw_input())
for i in range(t):
    ladder_list = {}
    sankes_list = {}
    ladders_count = int(raw_input())
    for j in range(ladders_count):
        s, e = map(int, raw_input().split(' '))
        ladders_list[s] = e
    snakes_count = int(raw_input())
    for j in range(sankes_count):
        s, e = map(int, raw_input().split(' '))
        snakes_list[s] = e
    print solve(ladders_list, snakes_list)


def solve(ladders, snakes):
    nodes = {}
    for i in range(1, 101):
        if i not in nodes:
            nodes[i] = node(i)
            if i not in ladders and i not in snakes:
                nodes[i+1] = node(i+1)
                nodes[i+2] = node(i+2)
                nodes[i+3] = node(i+3)
                nodes[i+4] = node(i+4)
                nodes[i+5] = node(i+5)
                nodes[i+6] = node(i+6)
                nodes[i].connections.append(nodes[i+1])
                nodes[i].connections.append(nodes[i+2])
                nodes[i].connections.append(nodes[i+3])
                nodes[i].connections.append(nodes[i+4])
                nodes[i].connections.append(nodes[i+5])
                nodes[i].connections.append(nodes[i+6])
            elif i in ladders:
                if ladders[i] not in nodes:
                    nodes[ladders[i]] = node(ladders[i])
                nodes[i].connections.append(nodes[ladders[i])
                
            elif i in snakes:
                if snakes[i] not in nodes:
                    nodes[snakes[i]] = node(snakes[i])
                nodes[i].connections.append(nodes[snakes[i]]) 




    



