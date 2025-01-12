
def solve_for_tokens(A, p):
    print(f'Solving with A : {A}, and p: {p}')
    determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if determinant == 0:
        print('No solution, det is 0')
        return 0
    A_inv = [[0, 0], [0, 0]]
    A_inv[0][0] = A[1][1] / determinant
    A_inv[1][1] = A[0][0] / determinant
    A_inv[0][1] = -A[0][1] / determinant
    A_inv[1][0] = -A[1][0] / determinant

    touches_a = A_inv[0][0]*p[0] + A_inv[0][1]*p[1]
    touches_b = A_inv[1][0]*p[0] + A_inv[1][1]*p[1]

    print(f'Tokens A: {touches_a}, Tokens B: {touches_b}')
    if touches_a < 0 or touches_b < 0:
        print('No solution, negative tokens')
        return 0
    elif abs(touches_a - round(touches_a)) >= 0.0001 or abs(touches_b - round(touches_b)) >= 0.0001:
        print('No solution, solution is a float')
        return 0
    else:
        return 3*round(touches_a) + round(touches_b)


with open("./aoc_day13/aoc_day13_test.txt") as f:
    data = f.read().strip().split('\n')
    print(data)
    data.append('')
    tokens = 0
    A = [[0, 0], [0, 0]]
    p = [0, 0]
    for line in data:
        print(line)
        if 'A' in line:
            x = int(line.split('X+')[1].split(',')[0])
            y = int(line.split('Y+')[1])
            print(x, y)
            A[0][0] = x
            A[1][0] = y
        if 'B' in line:
            x = int(line.split('X+')[1].split(',')[0])
            y = int(line.split('Y+')[1])
            print(x, y)
            A[0][1] = x
            A[1][1] = y
        if 'Prize' in line:
            x = int(line.split('X=')[1].split(',')[0])
            y = int(line.split('Y=')[1])
            print(x, y)
            p[0] = x + 10000000000000
            p[1] = y + 10000000000000
        if line == '':
            tokens += solve_for_tokens(A, p)
    print(tokens)