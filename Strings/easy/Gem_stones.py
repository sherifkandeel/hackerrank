def get_intersection(reference, s):
    intersection = ""
    for i in reference:
        if i in s: 
            intersection += i
    return intersection

stones = int(raw_input())
gem_stones = ""
for x in range(0, stones):
    stone = raw_input()
    stone = ''.join(set(stone))
    if x == 0:
        gem_stones = stone
        continue
    gem_stones = get_intersection(gem_stones, stone)
print len(gem_stones)

