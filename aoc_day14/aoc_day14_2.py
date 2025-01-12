def compute_danger_level(robot_positions):
    quadrants = {1: 0, 2: 0, 3: 0, 4: 0}
    for robot in robot_positions:
        px, py = robot[0]
        if px < 50 and py < 51:
            quadrants[1] += 1
        elif px > 50 and py < 51:
            quadrants[2] += 1
        elif px < 50 and py > 51:
            quadrants[3] += 1
        elif px > 50 and py > 51:
            quadrants[4] += 1
    return quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]

def pretty_print_as_grid(robot_positions):
    grid = [['.' for _ in range(101)] for _ in range(103)]
    for robot in robot_positions:
        px, py = robot[0]
        grid[py][px] = '#'
    for row in grid:
        print(''.join(row))

def compute_robot_positions_at_step(robot_positions, step):
    for robot in robot_positions:
        robot[0][0] = (robot[0][0] + step*robot[1][0]) % 101
        robot[0][1] = (robot[0][1] + step*robot[1][1]) % 103
    return robot_positions

with open("./aoc_day14/aoc_day14.txt") as f:
    data = f.read().strip().split('\n')
    print(data)
    robot_positions = []
    for line in data:
        p_part, v_part = line.split()
        px, py = map(int, p_part.replace('p=', '').split(','))
        vx, vy = map(int, v_part.replace('v=', '').split(','))
        robot_positions.append([[px, py], (vx, vy)])
    # list_of_danger_levels = []
    # for i in range(11000):
    #     for robot in robot_positions:
    #         robot[0][0] = (robot[0][0] + robot[1][0]) % 101
    #         robot[0][1] = (robot[0][1] + robot[1][1]) % 103
    #     list_of_danger_levels.append(compute_danger_level(robot_positions))
    #     pretty_print_as_grid(robot_positions)
    # print(list_of_danger_levels)
    # print(min(list_of_danger_levels))
    # print(list_of_danger_levels.index(min(list_of_danger_levels)))

    robot_positions = compute_robot_positions_at_step(robot_positions, 6512)
    pretty_print_as_grid(robot_positions)