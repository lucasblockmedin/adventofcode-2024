from aoc_day18_1 import astar, build_grid_from_input

with open('aoc_day18/aoc_day18.txt') as file:
    data = file.read().splitlines()
    grid_size = (71, 71)
    start = (0, 0)
    goal = (70, 70)
    idx = 1024
    while True:
        matrix = build_grid_from_input(data, grid_size, idx)
        path = astar(matrix, start, goal)
        if path:
            idx += 1
        else:
            print("No path found")
            break
    print("Final idx: ", idx)
    print(data[idx - 1])