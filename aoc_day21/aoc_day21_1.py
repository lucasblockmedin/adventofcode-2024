from itertools import product, permutations
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

def get_sequence(code, keypad):
    # We pass the code that we want to write at this level
    # and the keypad that we are currently on
    # We want to find the possible sequences that we can write 
    # print(f'Code: {code}')
    possibilities = []
    current_position = keypad['A']

    for element in code:
        next_position = keypad[element]
        # print(f'Current position: {current_position}, Next position: {next_position}')
        diff_i = next_position[0] - current_position[0]
        diff_j = next_position[1] - current_position[1]

        # We get the string of necessary combos to get to the next position
        moves = ''
        if diff_i > 0:
            moves += 'v' * diff_i
        elif diff_i < 0:
            moves += '^' * abs(diff_i)
        if diff_j > 0:
            moves += '>' * diff_j
        elif diff_j < 0:
            moves += '<' * abs(diff_j)
        # print(f'Moves: {moves}')
        all_moves = list(set([''.join(x) + 'A' for x in permutations(moves)]))
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
        possibilities.append(final_moves)
        # print(possibilities)
        current_position = next_position
    # print(possibilities)
    return [''.join(x) for x in product(*possibilities)]

def extract_number_from_string(string):
    return ''.join([char for char in string if char.isdigit()])

def find_shortest_sequence(sequences):
    print(f'Sequences: {sequences}')
    seq_1 = get_sequence(sequences, num_positions)
    seq_2 = []
    for seq in seq_1:
        seq_2 += get_sequence(seq, arrow_positions)
    seq_3 = []
    for seq in seq_2:
        seq_3 += get_sequence(seq, arrow_positions)
    return min([len(seq) for seq in seq_3])

with open('aoc_day21/aoc_day21.txt', 'r') as f:
    sequences = f.read().splitlines()
    total = 0
    for sequence in sequences:
        val = extract_number_from_string(sequence)
        shortest = find_shortest_sequence(sequence)
        total += shortest*int(val)
    print(total)