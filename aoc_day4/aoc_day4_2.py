
def find_x_mas(data, i, j):
    print(i,j)
    n = len(data)
    m = len(data[0])
    xmas = 0

    if i == 0 or j == 0 or i == n-1 or j == m-1:
        return 0
    
    cross_left_right = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
    print(cross_left_right)
    cross_right_left = data[i-1][j+1] + data[i][j] + data[i+1][j-1]
    print(cross_right_left)
    if (cross_left_right == 'MAS' or cross_left_right == 'SAM') and (cross_right_left == 'MAS' or cross_right_left == 'SAM'):
        print('X-MAS found')
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
            if char == 'A':
                print('A found')
                total_xmas += find_x_mas(data, i, j)
    print("TOTAL XMAS: ", total_xmas)
                