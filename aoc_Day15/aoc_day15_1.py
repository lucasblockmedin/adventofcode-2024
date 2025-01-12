DIRECTIONS = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

def pretty_print_warehouse(warehouse_matrix):
    for row in warehouse_matrix:
        print(''.join(row))

def update_map_with_instruction(warehouse_matrix, current_pos, direction):
    print("CURRENT POS: ", current_pos)
    new_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
    print("UPDATING MAP")
    print(f'Direction: {direction}')
    pretty_print_warehouse(warehouse_matrix)
    print(new_pos)
    if warehouse_matrix[new_pos[1]][new_pos[0]] == '#':
        print("HIT WALL, nothing changes")
        print("FINAL MAP")
        pretty_print_warehouse(warehouse_matrix)
        return current_pos
    elif warehouse_matrix[new_pos[1]][new_pos[0]] == 'O':
        print("HIT a box, can we push?")
        box_pos = new_pos
        while warehouse_matrix[box_pos[1]][box_pos[0]] != '#':
            if warehouse_matrix[box_pos[1]][box_pos[0]] == '.':
                print("Found a space, switching things")
                warehouse_matrix[box_pos[1]][box_pos[0]] = 'O'
                warehouse_matrix[new_pos[1]][new_pos[0]] = '@'
                warehouse_matrix[current_pos[1]][current_pos[0]] = '.'
                print("FINAL MAP")
                pretty_print_warehouse(warehouse_matrix)
                return new_pos
            else:
                print("Found another box, checking behind")
                box_pos = [box_pos[0] + direction[0], box_pos[1] + direction[1]]
        print("HIT WALL, nothing changes")
        return current_pos
    else:
        print("Just moving")
        warehouse_matrix[new_pos[1]][new_pos[0]] = '@'
        warehouse_matrix[current_pos[1]][current_pos[0]] = '.'
        print("FINAL MAP")
        pretty_print_warehouse(warehouse_matrix)
        return new_pos

def parse_for_boxes(warehouse_matrix):
    count = 0
    for i, row in enumerate(warehouse_matrix):
        for j, element in enumerate(row):
            if element == 'O':
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
            if '@' in line:
                current_pos = [line.index('@'), i]
            warehouse_matrix.append(list(line))
        else:
            instructions.extend(list(line))
    print(instructions)
    while instructions:
        instruction = instructions.pop(0)
        print(f'Instruction: {instruction}')
        current_pos = update_map_with_instruction(warehouse_matrix, current_pos, DIRECTIONS[instruction])

    parse_for_boxes(warehouse_matrix)