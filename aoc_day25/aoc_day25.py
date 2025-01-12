def create_key_or_lock(grid):
    key_or_lock = [-1, -1, -1, -1, -1]
    print(grid)
    for i in range(5):
        for j in range(7):
            # print(f'index: {i}, {j}')
            if grid[j][i] == '#':
                key_or_lock[i] += 1
    return key_or_lock

def check_key_lock(key, lock):
    for i in range(5):
        sum_heights = key[i] + lock[i]
        if sum_heights > 5:
            return False
    return True

def part1(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
        keys = []
        locks = []
        current = []
        is_key = False
        
        for line_num, line in enumerate(data):
            if current == []:
                if line[0] == '#':
                    is_key = False
                else:
                    is_key = True

            if line == '' or line_num == len(data) - 1:  # Check if we're at the last line
                # Add the current line before processing if we're at the end
                if line_num == len(data) - 1 and line != '':
                    current.append(line)
                
                # Process the pattern
                if is_key:
                    keys.append(create_key_or_lock(current))
                else:
                    locks.append(create_key_or_lock(current))
                current = []
                continue

            current.append(line)
        
        print(locks)
        print(keys)
        total_fits = 0
        for lock in locks:
            for key in keys:
                print(f'Key: {key}, Lock: {lock}')
                if check_key_lock(key, lock):
                    print('Good')
                    total_fits += 1
                    

        print(total_fits)
            
                

if __name__ == '__main__':
    part1('aoc_day25/aoc_day25.txt')
    # part1('aoc_day25/aoc_day25_input.txt')