
def can_form_string(target, base_strings, memo=None):
    # print("Checking target: ", target)
    # print("Base strings: ", base_strings)
    if memo is None:
        memo = {}
    
    if target in memo:
        return memo[target]
    
    if target == '':
        return True
        
    for base in base_strings:
        if target.startswith(base):
            # Recursively check if we can form the remaining string
            remaining = target[len(base):]
            if can_form_string(remaining, base_strings, memo):
                # Store result before returning
                memo[target] = True
                return True
    
    memo[target] = False
    return False

with open('aoc_day19/aoc_day19.txt') as f:
    data = f.read().splitlines()
    print(data)
    base_strings = data.pop(0).split(', ')
    print(base_strings)
    data.pop(0)
    count = 0
    for element in data:
        if can_form_string(element, base_strings):
            count += 1
    print(count)

