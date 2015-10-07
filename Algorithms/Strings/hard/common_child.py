s1 = raw_input()
s2 = raw_input()



def get_largest_common(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    s1_dict = {}
    s2_dict = {}
    for i in range(len(s1)):
        if s1_list[i] in s1_dict:
            s1_dict[s1_list[i]].append(i)
        else:
            s1_dict[s1_list[i]] = [i]

        if s2_list[i] in s2_dict:
            s2_dict[s2_list[i]].append(i)
        else:
            s2_dict[s2_list[i]] = [i]

    common_string = ''
    largest_idx = -1

    for c in s1_list:
        if c in s2_dict and s2_dict[c] > largest_idx:
            for item in s2_dict[c]:
                if item > largest_idx:
                    common_string += c
                    largest_idx = item
                    s2_dict[c].remove(item)
                    break
                        
    # print common_string
    return len(common_string)


maxm = 0
for i in range(len(s1)):
    sol1  = get_largest_common(s1[i:], s2)
    if sol1> maxm:
        maxm = sol1

for i in range(len(s2)):
    sol2 = get_largest_common(s2[i:], s1)
    if sol2> maxm:
        maxm = sol2


print maxm


