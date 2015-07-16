def get_lines(matrix):
    lines = []
    line = []
    for loop in range(len(matrix)/2):
        line = []
        for i in range(loop, len(matrix[0]) - loop):
            line.append(matrix[loop][i])
        for i in range(loop + 1, len(matrix) - loop - 1):
            line.append(matrix[i][len(matrix[0]) - 1 -loop])
        for i in range(len(matrix[0]) - 1 - loop, loop -1, -1):
            line.append(matrix[len(matrix) - 1 - loop][i])
        for i in range(len(matrix) - 2 - loop, loop , -1):
            line.append(matrix[i][loop])
        if len(line) > 0:
            lines.append(line)
    return lines


def construct_matrix(lines, m, n):
    constructed = [[0 for i in range(n)] for j in range(m)]
    for loop in range(len(lines)):
        line = lines[loop]
        # print m, n
        for i in range(len(line)):
            if i < n:
                constructed[loop][loop+i] = line[i]
            elif i < m+n - 2:
                constructed[i+loop - n +1][n-1+loop] = line[i]
            elif i < n+n+m -2:
                constructed[m - 1 + loop][(m - 2 +n+n) - i+loop - 1] = line[i]
            else:
                constructed[m + loop - 2 - (i - (n+m+n-2))][loop] = line[i]

        n = n - 2
        m = m - 2
        if m <=0 or n <=0:
            return constructed
    return constructed



def rotate_lines(lines, distance):
    rotated_lines = []
    normalized_distance = 0
    for line in lines:
        normalized_distance = distance % len(line)
        cut = line[0:normalized_distance]
        rest = line[normalized_distance:]
        rotated_lines.append(rest+cut)
    return rotated_lines


def rotate_matrix(matrix, distance, m, n):
    lines = get_lines(matrix)
    rotated_lines = rotate_lines(lines, distance)
    constructed = construct_matrix(rotated_lines, m, n)
    print "----------------------------------------------"
    for c in constructed:
        print ' '.join(map(str, c))


m, n, r = map(int, raw_input().split(' '))
matrix = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    line = map(int, raw_input().split(' '))
    for j in range(n):
        matrix[i][j] = line[j]

rotate_matrix(matrix, r, m, n)


