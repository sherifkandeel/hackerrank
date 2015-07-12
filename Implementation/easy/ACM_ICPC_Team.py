N, M = map(int, raw_input().split(' '))
people = [raw_input() for i in xrange(N)]

max_topics = 0
max_team_count = 0

for i in people:
    for j in people:
        if i==j: continue
        res = bin(int(i,2) | int(j,2)).count('1')
        if res > max_topics:
            max_topics = res
            max_team_count = 1
        elif res == max_topics:
            max_team_count += 1
print max_topics
print max_team_count/2
