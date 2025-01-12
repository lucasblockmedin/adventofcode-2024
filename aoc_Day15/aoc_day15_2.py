DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def pretty_print_warehouse(warehouse_matrix):
    for row in warehouse_matrix:
        print(''.join(row))


def move_robot(matrix, current_pos, direction):
    start_row, start_col = current_pos
    drow, dcol = direction
    stack = []
    to_visit = [(start_row, start_col)]
    visited = set()
    while to_visit:
        row, col = to_visit.pop()
        if (row, col) in visited or matrix[row][col] == '.':
            continue
        visited.add((row, col))
        if matrix[row][col] == '#':
            return current_pos
        stack.append((matrix[row][col], row, col))
        to_visit.append((row + drow, col + dcol))

        if matrix[row][col] == '[':
            to_visit.append((row, col + 1))
        elif matrix[row][col] == ']':
            to_visit.append((row, col - 1))

    print(stack)
    if direction == DIRECTIONS['^']:
        print('UP')
        stack = sorted(stack, key=lambda x: x[1], reverse=True)
    elif direction == DIRECTIONS['v']:
        print('DOWN')
        stack = sorted(stack, key=lambda x: x[1])
    elif direction == DIRECTIONS['<']:
        print('LEFT')
        stack = sorted(stack, key=lambda x: x[2], reverse=True)
    elif direction == DIRECTIONS['>']:
        print('RIGHT')
        stack = sorted(stack, key=lambda x: x[2])

    print(stack)

    while stack:
        char, row, col = stack.pop() 
        matrix[row+drow][col+dcol] = char
        matrix[row][col] = '.'
    
    return (start_row + drow, start_col + dcol)
        
def parse_for_boxes(matrix):
    count = 0
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == '[':
                print("Found a box")
                count += 100*i + j
    print(count)

with open("./aoc_Day15/aoc_day15.txt") as f:
    data = f.read().strip()
    print(data)
    data = data.split('\n')
    print(data)
    warehouse_matrix = []
    is_instructions = False
    instructions = []
    current_pos = [0, 0]
    for i, line in enumerate(data):
        if line == '':
            is_instructions = True
            continue
        if not is_instructions:
            j = 0
            line_list = []
            for element in line:
                if element == '#':
                    line_list.append('#')
                    line_list.append('#')
                    j += 2
                elif element == '.':
                    line_list.append('.')
                    line_list.append('.')
                    j += 2
                elif element == '@':
                    line_list.append('@')
                    line_list.append('.')
                    current_pos = [i, j]
                else:
                    line_list.append('[')
                    line_list.append(']')
                    j += 2
            warehouse_matrix.append(line_list)
        else:
            instructions.extend(list(line))
    print(instructions)
    pretty_print_warehouse(warehouse_matrix)


    while instructions:
        instruction = instructions.pop(0)
        print(f'Instruction: {instruction}')
        pretty_print_warehouse(warehouse_matrix)
        current_pos = move_robot(warehouse_matrix, current_pos, DIRECTIONS[instruction])
        pretty_print_warehouse(warehouse_matrix)

    parse_for_boxes(warehouse_matrix)

