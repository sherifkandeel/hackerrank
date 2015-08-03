n, k = map(int, raw_input().split(' '))
flowers = map(int, raw_input().split(' '))
flowers.sort(reverse=True)
people = [0 for x in range(k)]
summ = 0
for i in range(n):
    people[i%k] += 1
    summ += people[i%k]*flowers[i]
print summ
