
def compute_steps_and_quadrant(px, py, vx, vy, quadrants):
    grid_size_x = 101
    grid_size_y = 103
    px_100 = (px + 100*vx) % grid_size_x
    py_100 = (py + 100*vy) % grid_size_y
    print('Initial position', px, py)
    print('Velocity', vx, vy)
    print('Final position', px_100, py_100) 
    if px_100 < 50 and py_100 < 51:
        print('Quadrant 1')
        quadrants[1] += 1
    elif px_100 > 50 and py_100 < 51:
        print('Quadrant 2')
        quadrants[2] += 1
    elif px_100 < 50 and py_100 > 51:
        print('Quadrant 3')
        quadrants[3] += 1
    elif px_100 > 50 and py_100 > 51:
        print('Quadrant 4')
        quadrants[4] += 1

with open("./aoc_day14/aoc_day14.txt") as f:
    data = f.read().strip().split('\n')
    print(data)
    quadrants = {1: 0, 2: 0, 3: 0, 4: 0}
    for line in data:
        print(line)
        p_part, v_part = line.split()
        px, py = map(int, p_part.replace('p=', '').split(','))
        vx, vy = map(int, v_part.replace('v=', '').split(','))
        compute_steps_and_quadrant(px, py, vx, vy, quadrants)
    print(quadrants)
    safety_factor = quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]
    print(safety_factor)
        
        
    