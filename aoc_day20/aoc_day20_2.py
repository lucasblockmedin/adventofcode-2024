from collections import defaultdict, deque
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

def precompute_distances(data, end):
    distances = defaultdict(lambda: float('inf'))
    initial_state = (end[0], end[1])
    distances[initial_state] = 0
    heap = [(0, initial_state)]
    
    while heap:
        current_distance, current_state = heapq.heappop(heap)
        
        for drow, dcol in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_row = current_state[0] + drow
            new_col = current_state[1] + dcol
            
            if data[new_row][new_col] == '#':
                continue
                
            new_state = (new_row, new_col)
            new_distance = current_distance + 1
            
            if new_distance < distances[new_state]:
                distances[new_state] = new_distance
                heapq.heappush(heap, (new_distance, new_state))
    
    return distances

def find_cheats_flood_fill(data, start_pos, path_index, end_distances, baseline_time):
    queue = deque([(start_pos, 0)])  # (position, moves_used)
    visited = set()  # Track (position, moves) pairs we've seen
    unique_cheats = set()  # Track unique (start_pos, end_pos) pairs
    
    while queue:
        pos, moves = queue.popleft()
        
        if (pos, moves) in visited:
            continue
        visited.add((pos, moves))
            
        # If we're on a track, check if this is a valid cheat
        if data[pos[0]][pos[1]] != '#':
            total_time = path_index + moves + end_distances[pos]
            saving = baseline_time - total_time
            if saving >= 100:
                cheat_pair = (start_pos, pos)  # The unique cheat identifier
                unique_cheats.add(cheat_pair)
        
        # Continue flood fill if we have moves left
        if moves < 20:
            for drow, dcol in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_pos = (pos[0] + drow, pos[1] + dcol)
                if (0 <= new_pos[0] < len(data) and 
                    0 <= new_pos[1] < len(data[0])):
                    queue.append((new_pos, moves + 1))
    
    return len(unique_cheats)  # Return number of unique cheats found

def find_best_cheats(data, path, end, baseline_time):
    print("Starting search for cheats")
    print(f"Path length: {len(path)}")
    print(f"Baseline time: {baseline_time}")
    
    # Precompute distances from all points to end
    end_distances = precompute_distances(data, end)
    print(f"Precomputed distances to end for {len(end_distances)} positions")
    
    count = 0
    for i, pos in enumerate(path):
        print(f"\nChecking path position {i}: {pos}")
        count += find_cheats_flood_fill(data, pos, i, end_distances, baseline_time)
        
    print(f"\nTotal cheats found: {count}")
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


