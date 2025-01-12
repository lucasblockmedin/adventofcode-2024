from collections import defaultdict
import heapq


def find_shortest_path(data):
    start = (len(data)-2, 1)
    end = (1, len(data[0])-2)

    initial_state = (start[0], start[1], 1)

    distances = defaultdict(lambda: float('inf'))
    distances[initial_state] = 0

    predecessors = defaultdict(list)
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
            new_distance = current_distance + 1  # base movement cost
            if current_state[2] != i:
                new_distance += 1000

            new_state = (new_row, new_col, i)
            
            if new_distance <= distances[new_state]:
                if new_distance < distances[new_state]:
                    predecessors[new_state].clear()
                    distances[new_state] = new_distance
                    heapq.heappush(heap, (new_distance, new_state))
                    
                predecessors[new_state].append(current_state)
    
    end_states = [(end[0], end[1], d) for d in range(4)]
    best_end_state = min(end_states, key=lambda s: distances[s])
    best_end_states = [s for s in end_states if distances[s] == distances[best_end_state]]

    def reconstruct_paths(state):
        if state[0:2] == (start[0], start[1]):
            return [[state[0:2]]]
        
        paths = []
        for pred in predecessors[state]:
            for path in reconstruct_paths(pred):
                paths.append(path + [state[0:2]])
        return paths
    
    all_paths = []
    for best_end_state in best_end_states:
        path = reconstruct_paths(best_end_state)
        all_paths.extend(path)
    
    print(all_paths)
    final_set = set()
    for path in all_paths:
        for element in path:
            final_set.add(element)
    print(len(final_set))

    return distances[best_end_state]
        

with open('./aoc_day16/input-maria.txt') as f:
    data = f.read().strip().split('\n')
    # print(data)
    res = find_shortest_path(data)
    print(res)