import copy
from tqdm import tqdm

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

def there_is_a_loop(base_map, direction, position):
    n = len(base_map)
    m = len(base_map[0])
    there_is_a_loop = False
    current_position = position
    while True:
        new_position = [
            current_position[0] + MOVING_DIRECTION[direction][0], 
            current_position[1] + MOVING_DIRECTION[direction][1]
        ]
        
        if gets_out_of_map(new_position, n, m):
            break
        
        map_info_new_position = base_map[new_position[0]][new_position[1]]
        if map_info_new_position == (-1, []):
            # Turn ninety degrees
            direction = NINETY_DEGREES[direction]
            continue

        if map_info_new_position[0] >= 1 and direction in map_info_new_position[1]:
            there_is_a_loop = True
            break
        new_directions = map_info_new_position[1] + [direction]
        base_map[new_position[0]][new_position[1]] = (map_info_new_position[0] + 1, new_directions)
        current_position = new_position

    return there_is_a_loop

def pretty_print(matrix):
    for row in matrix:
        print(row)
    print()

def build_base_matrix(entry_table):
    base_map = entry_table.copy()
    for i, row in enumerate(entry_table):
        for j, column in enumerate(row):
            if column == ".":
                base_map[i][j] = (0, [])
            elif column == "#":
                base_map[i][j] = (-1, [])
            elif column in ["^", "v", "<", ">"]:
                base_map[i][j] = (1, [column])
                direction = column
                position = [i, j]
            
    return base_map, direction, position

def gets_out_of_map(new_position, n, m):
    new_i, new_j = new_position
    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
        return True
    return False


with open('./aoc_day6/aoc_day6.txt', 'r') as file:
    data = file.read()
    entry_table = data.split('\n')
    for i, entry in enumerate(entry_table):
        entry_table[i] = list(entry)
    base_map, direction, position = build_base_matrix(entry_table)
    number_of_loops = 0
    for i in tqdm(range(len(base_map)), desc="Rows"):
        for j in tqdm(range(len(base_map[0])), desc="Columns", leave=False):
            if base_map[i][j] == (0, []):
                test_map = copy.deepcopy(base_map)
                test_map[i][j] = (-1, [])
                if there_is_a_loop(test_map, direction, position):
                    number_of_loops += 1
    print(number_of_loops)

