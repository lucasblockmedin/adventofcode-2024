
def find_xmas(data, i, j):
    print(i,j)
    n = len(data)
    m = len(data[0])
    directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    xmas = 0

    for direction in directions:
        count = 0
        for l in range(1, 4):
            new_i = i + l * direction[0]
            new_j = j + l * direction[1]
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                break
            if data[new_i][new_j] == 'MAS'[l-1]:
                count += 1
            else:
                break
        if count == 3:
            xmas += 1
    return xmas



with open('./aoc_day4/aoc_day4.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()
    print(data)
    total_xmas = 0
    for i, line in enumerate(data):
        for j,char in enumerate(line):
            if char == 'X':
                print('X found')
                total_xmas += find_xmas(data, i, j)
    print(total_xmas)
                