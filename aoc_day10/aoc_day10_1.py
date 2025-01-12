from collections import deque

def add_surrounding_nodes(data, node, explored_nodes, n, m):
    x = node[1]
    y = node[2]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if int(data[nx][ny]) - node[0] == 1:
            explored_nodes.appendleft((int(data[nx][ny]), nx, ny))

def find_all_paths(data, node):
    n, m = len(data), len(data[0])
    print(f"Starting node: {node}")
    explored_nodes = deque()
    explored_nodes.appendleft(node)
    while explored_nodes:
        node = explored_nodes.pop()
        if node[0] == 9:
            explored_nodes.appendleft(node)
            print('set of explored nodes:', set(explored_nodes))
            return len(set(explored_nodes))
        add_surrounding_nodes(data, node, explored_nodes, n, m)
        print(explored_nodes)
    return 0


with open('./aoc_day10/aoc_day10.txt') as f:
    data = f.read()
    data = data.split('\n')
    print(data)
    count = 0
    for i, line in enumerate(data):
        print(i, line)
        for j, char in enumerate(line):
            if char == '0':
                count += find_all_paths(data, (0, i, j))
                
    print(count)