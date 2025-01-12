import math

with open("aoc_day17/aoc_day17.txt", "r") as f:
    lines = f.read().splitlines()
    print(lines)
    reg_a = 0
    reg_b = 0
    reg_c = 0
    program = []
    for line in lines:
        if "Register A" in line:
            reg_a = int(line.split(":")[1].strip())
        elif "Register B" in line:
            reg_b = int(line.split(":")[1].strip())
        elif "Register C" in line:
            reg_c = int(line.split(":")[1].strip())
        elif "Program" in line:
            program = line.split(":")[1].strip().split(",")
            print(program)
    
    index = 0
    output = []
    while index < len(program):
        operator = program[index]
        operand = program[index + 1]
        og_operand = operand
        if operand in ['0', '1', '2', '3']:
            operand = int(operand)
        elif operand == '4':
            operand = int(reg_a)
        elif operand == '5':
            operand = int(reg_b)
        elif operand == '6':
            operand = int(reg_c)
        
        if operator == '0':
            print("ADV")
            reg_a = math.trunc(reg_a/(2**operand))
            index += 2
        elif operator == '1':
            print("BXL")
            reg_b = reg_b^int(og_operand)
            index += 2
        elif operator == '2':
            print("BST")
            reg_b = operand % 8
            index += 2
        elif operator == '3':
            print("JNZ")
            if reg_a != 0:
                index = int(og_operand)
            else:
                index += 2
        elif operator == '4':
            print("BXC")
            reg_b = reg_b^reg_c
            index += 2
        elif operator == '5':
            print("OUT")
            output.append(str(operand%8))
            index += 2
        elif operator == '6':
            print("BDV")
            reg_b = math.trunc(reg_a/(2**operand))
            index += 2
        elif operator == '7':
            print("CDV")
            reg_c = math.trunc(reg_a/(2**operand))
            index += 2

        print(reg_a, reg_b, reg_c)
    print(",".join(output))