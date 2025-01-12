MOVING_DIRECTION = {
    "^": [-1, 0],
    "v": [1, 0],
    "<": [0, -1],
    ">": [0, 1]
}
NINETY_DEGREES = {
    "^": ">",
    "v": "<",
    "<": "^",
    ">": "v"
}

def pretty_print(matrix):
    for row in matrix:
        print(row)
    print()

def build_base_matrix(entry_table):
    base_map = entry_table.copy()
    for i, row in enumerate(entry_table):
        for j, column in enumerate(row):
            if column == ".":
                base_map[i][j] = 0
            elif column == "#":
                base_map[i][j] = -1
            elif column in ["^", "v", "<", ">"]:
                base_map[i][j] = 1
                direction = column
                position = [i, j]
            
    return base_map, direction, position

def gets_out_of_map(new_position, n, m):
    new_i, new_j = new_position
    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
        return True
    return False

def count_number_of_visited_cells(base_map, direction, position):
    pretty_print(base_map)
    n = len(base_map)
    m = len(base_map[0])
    visited_cells = 0
    current_position = position

    while True:
        new_position = [
            current_position[0] + MOVING_DIRECTION[direction][0], 
            current_position[1] + MOVING_DIRECTION[direction][1]
        ]
        
        if gets_out_of_map(new_position, n, m):
            break
            
        if base_map[new_position[0]][new_position[1]] == -1:
            # Recursion only when we need to turn
            new_direction = NINETY_DEGREES[direction]
            visited_cells += count_number_of_visited_cells(base_map, new_direction, current_position)
            break
            
        if base_map[new_position[0]][new_position[1]] == 0:
            visited_cells += 1
            
        base_map[new_position[0]][new_position[1]] += 1
        current_position = new_position
        
    return visited_cells


with open('./aoc_day6/aoc_day6.txt', 'r') as file:
    data = file.read()
    entry_table = data.split('\n')
    for i, entry in enumerate(entry_table):
        entry_table[i] = list(entry)
    base_map, direction, position = build_base_matrix(entry_table)
    print(count_number_of_visited_cells(base_map, direction, position) + 1) # +1 because we start at 1