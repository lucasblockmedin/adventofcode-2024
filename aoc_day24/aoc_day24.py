def apply_AND(val1, val2):
    return val1 & val2

def apply_OR(val1, val2):
    return val1 | val2

def apply_XOR(val1, val2):
    return val1 ^ val2

def run_all_operations(existing_memory, nb_of_z, operations):
    while operations:
        if nb_of_z == 0:
            break
        operation = operations.pop(0)
        left, op, right, output = operation
        if left in existing_memory and right in existing_memory:
            val1 = existing_memory[left]
            val2 = existing_memory[right]
            if op == 'AND':
                result = apply_AND(val1, val2)
            elif op == 'OR':
                result = apply_OR(val1, val2)
            elif op == 'XOR':
                result = apply_XOR(val1, val2)
            existing_memory[output] = result
            if output.startswith('z'):
                nb_of_z -= 1
        else:
            operations.append(operation)
    return existing_memory, nb_of_z

def part1(filename):
    with open(filename, 'r') as f:
        existing_memory = {}
        operations = []
        nb_of_z = 0
        is_memory = True
        for line in f:
            print(line)
            if line == '\n':
                is_memory = False
                continue
            if is_memory:
                memory, value = line.strip().split(': ')
                existing_memory[memory] = int(value)
            else:
                operation_str, output = line.strip().split(' -> ')
                left, op, right = operation_str.split(' ')
                operation = (left, op, right, output)
                operations.append(operation)
                if output.startswith('z'):
                    nb_of_z += 1

        print(existing_memory)
        print(operations)
        result, _ = run_all_operations(existing_memory, nb_of_z, operations)
        print(result)
        # We want to keep a dict with only the elements that start with 'z'
        # and then sum their values
        z_values = {key: value for key, value in result.items() if key.startswith('z')}
        z_values_sorted = sorted(z_values.keys())
        print(z_values_sorted)
        binary_value = ''.join([str(z_values[key]) for key in reversed(z_values_sorted)])
        print(binary_value)
        decimal_value = int(binary_value, 2)
        print(decimal_value)

'''
The second part of the problem relies on seeing that what we are building with the gates is a ripple carry adder
Therefore, we can see how it is built and understand how to find operations that are wrong
Because output = (a XOR b) XOR c -> if output is z gate must be a xor (unless it is the last op)
And if the output is carry, c = (a and b) or ((a xor b) and c) -> if output is not z gate and inputs are not x and y, then op has to be and or or
-> This way we can find part of the answer
# Rule 3: XOR with x,y inputs must feed into another XOR
# Rule 4: AND must feed into OR
'''

def find_incorrect_operations(operations):
    incorrect_operations = []
    
    # Track gate connections - will map each gate's output variable to its inputs
    input_to_operations = {}  # Maps each input to all operations that use it
    
    # Build input_to_operations mapping
    for operation in operations:
        left, op, right, output = operation
        # Track which operations use 'left' as input
        if left not in input_to_operations:
            input_to_operations[left] = []
        input_to_operations[left].append(operation)
        # Track which operations use 'right' as input
        if right not in input_to_operations:
            input_to_operations[right] = []
        input_to_operations[right].append(operation)

    print(input_to_operations)

    for operation in operations:
        left, op, right, output = operation
        if output.startswith('z'):
            if '45' in output:
                continue
            if op != 'XOR':
                print('Rule 1, adding', operation)
                incorrect_operations.append(operation)
                continue

        elif not left.startswith('x') and not left.startswith('y') and not right.startswith('x') and not right.startswith('y'):
            if op != 'AND' and op != 'OR':
                print('Rule 2, adding', operation)
                incorrect_operations.append(operation)
                continue
        
        if op == 'XOR' and (left.startswith('x') or left.startswith('y')) and \
           (right.startswith('x') or right.startswith('y')):
            if right == 'x00' or right == 'y00':
                continue
            else:
                has_xor_follower = any(
                    following_op[1] == 'XOR' 
                    for following_op in input_to_operations[output]
                )
                if not has_xor_follower and not left.startswith('x00'):
                    print(f'Output: {output}, Operation: {operation}')
                    print('Rule 3, adding', operation)
                    incorrect_operations.append(operation)
                    continue
        
        if op == 'AND':
            has_or_follower = any(
                following_op[1] == 'OR' 
                for following_op in input_to_operations[output]
            )
            if not has_or_follower and not left.startswith('x00'):
                print(f'Output: {output}, Operation: {operation}')
                print('Rule 4, adding', operation)
                incorrect_operations.append(operation)
                continue
    
    return incorrect_operations

def part2(filename):
    with open(filename, 'r') as f:
        existing_memory = {}
        operations = []
        nb_of_z = 0
        is_memory = True
        for line in f:
            print(line)
            if line == '\n':
                is_memory = False
                continue
            if is_memory:
                memory, value = line.strip().split(': ')
                existing_memory[memory] = int(value)
            else:
                operation_str, output = line.strip().split(' -> ')
                left, op, right = operation_str.split(' ')
                operation = (left, op, right, output)
                operations.append(operation)
                if output.startswith('z'):
                    nb_of_z += 1
    
        incorrect_ops = find_incorrect_operations(operations)
        print(incorrect_ops)
        

if __name__ == '__main__':
    part1('aoc_day24/aoc_day24.txt')
    part2('aoc_day24/aoc_day24.txt')
