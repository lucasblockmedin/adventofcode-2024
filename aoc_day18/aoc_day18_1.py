from heapq import heappush, heappop

def manhattan_distance(p1, p2) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def astar(matrix, start, goal):
    """A* algorithm."""
    def heuristic(a, b) -> int:
        """Calculate the heuristic value between two points
        using Manhattan distance."""
        return manhattan_distance(a, b)

    row, cols = len(matrix), len(matrix[0])

    p_queue = [(manhattan_distance(start, goal), start)]
    visited_nodes = set()
    track_path = {}
    g_cost = {start: 0}

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while p_queue:
        current_f, current = heappop(p_queue)

        if current == goal:
            path = []
            while current in track_path:
                path.append(current)
                current = track_path[current]
            path.append(start)
            return path[::-1]

        visited_nodes.add(current)
        for d in directions:
            next_node = (current[0] + d[0], current[1] + d[1])

            if next_node[0] < 0 or next_node[0] >= row or next_node[1] < 0 or next_node[1] >= cols:
                continue
            elif next_node in visited_nodes:
                continue
            elif matrix[next_node[0]][next_node[1]] == 1:
                continue
            

            new_cost = g_cost[current] + 1
            if next_node not in g_cost or new_cost < g_cost[next_node]:
                track_path[next_node] = current
                g_cost[next_node] = new_cost
                f_score = new_cost + heuristic(next_node, goal)
                heappush(p_queue, (f_score, next_node))
    return None

def build_grid_from_input(data, grid_size, nb_bytes_to_read):
    n, m = grid_size
    matrix = [[0 for col in range(m)] for row in range(n)]
    for i in range(nb_bytes_to_read):
        object_coord = data[i].split(',')
        a, b = int(object_coord[0]), int(object_coord[1])
        # print(a, b)
        matrix[a][b] = 1
    return matrix

def pretty_print_matrix(matrix):
    for row in matrix:
        print(row)

with open('aoc_day18/aoc_day18.txt') as file:
    data = file.read().splitlines()
    print(data)
    grid_size = (71, 71)
    nb_bytes_to_read = 1024
    matrix = build_grid_from_input(data, grid_size, nb_bytes_to_read)
    pretty_print_matrix(matrix)
    start = (0, 0)
    goal = (70, 70)
    path = astar(matrix, start, goal)
    print(path)
    print(len(path) - 1)

            
