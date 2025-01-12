from functools import lru_cache

def mix_into_secret_number(current_secret, value_to_mix):
    return current_secret ^ value_to_mix

def prune_secret_number(secret):
    return secret % 16777216

def step_1(secret):
    secret64 = secret * 64
    mixed = mix_into_secret_number(secret, secret64)
    return prune_secret_number(mixed)

def step_2(secret):
    secretdiv32 = secret // 32
    mixed = mix_into_secret_number(secret, secretdiv32)
    return prune_secret_number(mixed)

def step_3(secret):
    secret2048 = secret * 2048
    mixed = mix_into_secret_number(secret, secret2048)
    return prune_secret_number(mixed)

@lru_cache(maxsize=None)
def compute_transformation(secret):
    secret = step_1(secret)
    secret = step_2(secret)
    secret = step_3(secret)
    return secret

def part1(filename):
    with open(filename, 'r') as file:
        res = 0
        data = file.read().strip()
        print(data)
        for line in data.split('\n'):
            secret = int(line)
            for _ in range(2000):
                secret = compute_transformation(secret)
                # print('Intermediate secret:', secret)
            # print(f'Result for number {line}: {secret}')
            res += secret
    print(res)

def get_all_sequences(secret):
    digits = [secret % 10]
    for _ in range(2000):
        secret = compute_transformation(secret)
        digits.append(secret % 10)
    # print(digits)
    differences = []
    for i in range(1, len(digits)):
        diff = digits[i] - digits[i-1]
        differences.append(diff)
    # print(differences)
    
    sequences = []
    for i in range(len(differences) - 3):  
        diff_sequence = tuple(differences[i:i+4])
        next_digit = digits[i+4]
        sequences.append((diff_sequence, next_digit))
    # print(sequences)
    return sequences

def part2(filename):
    sequence_sums = {}  
    
    with open(filename, 'r') as file:
        starter_secrets = [int(line) for line in file.read().strip().split('\n')]
    
    for secret in starter_secrets:
        print(f"Processing secret: {secret}")
        sequences = get_all_sequences(secret)

        seen_sequences = set()
        
        for seq, next_digit in sequences:
            if seq not in seen_sequences:
                sequence_sums[seq] = sequence_sums.get(seq, 0) + next_digit
                seen_sequences.add(seq)
    best_sequence = max(sequence_sums.items(), key=lambda x: x[1])
    print(f"Best sequence: {best_sequence[0]}")
    print(f"Total sum: {best_sequence[1]}")


if __name__ == '__main__':
    # part1('aoc_day22/aoc_day22.txt')
    part2('aoc_day22/aoc_day22.txt')