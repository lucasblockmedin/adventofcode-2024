from itertools import combinations
from functools import lru_cache

num_positions = {
        '7': (0,0), '8': (0,1), '9': (0,2),
        '4': (1,0), '5': (1,1), '6': (1,2),
        '1': (2,0), '2': (2,1), '3': (2,2),
        '0': (3,1), 'A': (3,2)
    }

arrow_positions = {
        '^': (0,1), 'A': (0,2),
        '<': (1,0), 'v': (1,1), '>': (1,2)
    }

symbol_to_diff = {
        'v': (1,0), '^': (-1,0), '>': (0,1), '<': (0,-1)
    }

def get_moves(char_a, int_a, char_b, int_b):
    # The idea of this function is that it avoids the duplicates that are created because of permutations
    # Since combination allows us to differentiate between the two characters, we can use it to avoid duplicates
    for i in combinations(range(int_a + int_b), r=int_a):
        res = [char_b] * (int_a + int_b)
        for j in i:
            res[j] = char_a
        yield ''.join(res)



@lru_cache(maxsize=None)
def get_sequence(a, b, keypad):
    # We pass the point that we are currently on and the point that we want to go to
    # and the keypad that we are currently on
    # We want to find the possible sequences that we can write 
    keypad = num_positions if not keypad else arrow_positions
    print(keypad)
    current_position = keypad[a]
    next_position = keypad[b]
    # print(f'Current position: {current_position}, Next position: {next_position}')
    diff_i = next_position[0] - current_position[0]
    diff_j = next_position[1] - current_position[1]
    print(f'Diff i: {diff_i}, Diff j: {diff_j}')

    # We get the string of necessary combos to get to the next position
    moves = []
    if diff_i > 0:
        moves += ['v', diff_i]
    else:
        moves += ['^', abs(diff_i)]
    if diff_j > 0:
        moves += ['>', diff_j]
    else:
        moves += ['<', abs(diff_j)]
    print(f'Moves: {moves}')
    all_moves = list(set([''.join(x) + 'A' for x in get_moves(*moves)]))
    # print(f'All moves: {all_moves}')
    final_moves = []
    for move in all_moves:
        curr_i, curr_j = current_position
        is_usable = True
        for m in move[:-1]: # We don't want to move to the last position A
            d_i, d_j = symbol_to_diff[m]
            curr_i, curr_j = curr_i + d_i, curr_j + d_j
            # print(f'Current position: {curr_i, curr_j}')
            if (curr_i, curr_j) not in keypad.values():
                # print(f'Invalid move: {move}')
                is_usable = False
                break
        if is_usable:
            final_moves.append(move)
    return final_moves

@lru_cache(maxsize=None)
def get_cost(a, b, keypad, depth=0):
    if depth == 0:
        assert keypad
        return min([len(x) for x in get_sequence(a, b, keypad)])
    
    possible_sequences = get_sequence(a, b, keypad)
    print(f'Possible sequences: {possible_sequences}')
    best_cost = 1<<60 # Infinity, it is a way to define a very large integer that still fits in 64 bits
    for seq in possible_sequences:
        seq = 'A' + seq
        cost = 0
        for i in range(len(seq) - 1):
            cost += get_cost(seq[i], seq[i+1], True, depth - 1)
        best_cost = min(best_cost, cost)
    return best_cost

def get_code_cost(code):
    code = 'A' + code
    cost = 0
    for i in range(len(code) - 1):
        cost += get_cost(code[i], code[i+1], False, 25)
    return cost

def extract_number_from_string(string):
    return ''.join([char for char in string if char.isdigit()])

with open('aoc_day21/aoc_day21.txt', 'r') as f:
    sequences = f.read().splitlines()
    total = 0
    for sequence in sequences:
        val = extract_number_from_string(sequence)
        shortest = get_code_cost(sequence)
        total += shortest*int(val)
    print(total)