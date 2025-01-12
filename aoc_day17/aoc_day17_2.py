import math

def execute_program(reg_a, match_digits, program=['2', '4', '1', '3', '7', '5', '0', '3', '1', '5', '4', '1', '5', '5', '3', '0']):
    print("We tested this number: ", reg_a)

    index = 0
    output = []
    reg_b = 0
    reg_c = 0
    while index < len(program):
        operator = program[index]
        operand = program[index + 1]
        og_operand = operand
        
        # Convert operand to appropriate value
        if operand in ['0', '1', '2', '3']:
            operand = int(operand)
        elif operand == '4':
            operand = int(reg_a)
        elif operand == '5':
            operand = int(reg_b)
        elif operand == '6':
            operand = int(reg_c)
            
        # Execute instructions
        if operator == '0':    # ADV
            reg_a = math.trunc(reg_a/(2**operand))
            index += 2
        elif operator == '1':   # BXL
            reg_b = reg_b^int(og_operand)
            index += 2
        elif operator == '2':   # BST
            reg_b = operand % 8
            index += 2
        elif operator == '3':   # JNZ
            if reg_a != 0:
                index = int(og_operand)
            else:
                index += 2
        elif operator == '4':   # BXC
            reg_b = reg_b^reg_c
            index += 2
        elif operator == '5':   # OUT
            output.append(str(operand%8))
            index += 2
        elif operator == '6':   # BDV
            reg_b = math.trunc(reg_a/(2**operand))
            index += 2
        elif operator == '7':   # CDV
            reg_c = math.trunc(reg_a/(2**operand))
            index += 2
            
    output_str = "".join(output)
    
    # Check if the last n digits match
    program_str = "".join(program)
    matches = output_str[-match_digits:] == program_str[-match_digits:]
    print("Program: ", program_str)
    print("Output: ", output_str)
    print("Matches: ", matches)
    
    return matches, output_str


def explore_valid_numbers(total_iterations):
    def check_number(num, depth):
        matches, _ = execute_program(num, depth)
        return matches
    
    def dfs(current_num, depth):
        # Base case: if we've done all iterations
        if depth == total_iterations:
            return [current_num]
            
        results = []
        # Try adding each digit (0-7)
        for digit in range(8):
            next_num = current_num * 8 + digit
            if check_number(next_num, depth + 1):
                results.extend(dfs(next_num, depth + 1))
        
        return results
    
    # Start with digits 0-7
    all_valid = []
    for digit in range(8):
        if check_number(digit, 1):
            results = dfs(digit, 1)
            all_valid.extend(results)
    
    return sorted(all_valid) if all_valid else None

# Test the implementation
def test_implementation():
    target_length = 16
    result = explore_valid_numbers(target_length)
    
    if result:
        print(f"\nFound valid numbers: {result}")
        for num in result:
            print(f"\nValidating number: {num}")
            is_valid, output = execute_program(num, target_length)
            print(f"Valid: {is_valid}")
            print(f"In base 8: {oct(num)[2:]}")
    else:
        print("No valid numbers found")
    
    return result

if __name__ == "__main__":
    print(min(test_implementation()))