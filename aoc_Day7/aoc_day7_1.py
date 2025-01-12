def try_sign(goal, acc, numbers, index):
    if index == len(numbers):
        if goal == acc:
            return True
        else:
            return False
    
    if acc > goal:
        return False
    
    with_multiply_operator = try_sign(goal, acc*numbers[index], numbers, index+1)
    with_plus_operator = try_sign(goal, acc+numbers[index], numbers, index+1)

    return with_multiply_operator or with_plus_operator

with open('./aoc_day7/aoc_day7.txt') as f:
    data = f.read()
    data = data.split('\n')
    possible_operators = ['+', '*']
    sum_valid_res = 0
    for line in data:
        separated_eq = line.split(':')
        res = int(separated_eq[0])
        numbers = separated_eq[1]
        list_of_numbers = numbers.split(' ')[1:]
        list_of_numbers = [int(x) for x in list_of_numbers]
        if try_sign(res, list_of_numbers[0], list_of_numbers, 1):
            sum_valid_res += res
        
    print(sum_valid_res)
        
        


