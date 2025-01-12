from collections import defaultdict
import heapq

from functools import lru_cache

def find_shortest_path(data, start, end):

    initial_state = (start[0], start[1])

    distances = defaultdict(lambda: float('inf'))
    distances[initial_state] = 0

    predecessors = {}
    heap = [(0, initial_state)]

    direction_to_delta = {
        0: (0, 1),   # right
        1: (-1, 0),  # up
        2: (0, -1),  # left
        3: (1, 0)    # down
    }

    while heap:
        current_distance, current_state = heapq.heappop(heap)
        if (current_state[0], current_state[1]) == end:
            break
        for i in range(4):
            drow, dcol = direction_to_delta[i]
            new_row = current_state[0] + drow
            new_col = current_state[1] + dcol
            if data[new_row][new_col] == '#':
                continue
            new_state = (new_row, new_col)
            new_distance = current_distance + 1
        
            if new_distance < distances[new_state]:
                distances[new_state] = new_distance
                heapq.heappush(heap, (new_distance, new_state))
                predecessors[new_state] = current_state

    
    return predecessors

@lru_cache(maxsize=None)
def find_shortest_path_cached(data_tuple, start, end):
    # Convert tuple back to list since we can't hash lists for caching
    data = list(data_tuple)
    return find_shortest_path(data, start, end)


def get_main_path(predecessors, start):
    path = []
    current = start
    while current in predecessors:
        path.append(current)
        current = predecessors[current]
    path.append(current)  # Add start position
    return path[::-1]

def get_possible_cheat_ends(data, pos):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cheat_ends = []
    
    for first_move in directions:
        pos_after_first = (pos[0] + first_move[0], pos[1] + first_move[1])
        if 0 <= pos_after_first[0] < len(data) and 0 <= pos_after_first[1] < len(data[0]):
            for second_move in directions:
                final_pos = (pos_after_first[0] + second_move[0], 
                           pos_after_first[1] + second_move[1])
                # Final position must be in bounds and on track
                if (0 <= final_pos[0] < len(data) and 
                    0 <= final_pos[1] < len(data[0]) and 
                    data[final_pos[0]][final_pos[1]] != '#'):
                    cheat_ends.append(final_pos)
    return cheat_ends

def find_best_cheats(data, path, end, baseline_time):
    count = 0
    
    # Cache for end-to-E distances
    end_distances = {}
    
    for i, pos in enumerate(path):
        time_to_cheat_start = i
        
        for cheat_end in get_possible_cheat_ends(data, pos):
            if cheat_end not in end_distances:
                predecessors = find_shortest_path_cached(tuple(data), cheat_end, end)
                end_distances[cheat_end] = len(get_main_path(predecessors, end))
            time_from_cheat_end = end_distances[cheat_end]
            
            total_time = time_to_cheat_start + 2 + time_from_cheat_end
            saving = baseline_time - total_time
            
            if saving >= 99:
                count += 1
    
    return count

with open('aoc_day20/aoc_day20.txt') as f:
    data = f.read().splitlines()
    print(data)
    for i, line in enumerate(data):
        for j, element in enumerate(line):
            if element == 'S':
                start = (i, j)
            elif element == 'E':
                end = (i, j)
    pred = find_shortest_path_cached(tuple(data), start, end)
    path = get_main_path(pred, end)
    result = find_best_cheats(data, path, end, len(path)-1)

    print(start)
    print(end)
    print(path)
    print(len(path)-1)
    print(result)

    

