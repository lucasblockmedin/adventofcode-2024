def sort_order(rules_dict, printing_list):
    for i, element in enumerate(printing_list):
        if i == 0 or not rules_dict.get(int(element)):
            continue
        
        if int(printing_list[i-1]) in rules_dict[int(element)]:
            for j in range(i-1, -1, -1):
                if int(printing_list[j]) in rules_dict[int(element)]:
                    printing_list[j], printing_list[j+1] = printing_list[j+1], printing_list[j]
                else:
                    break
    return printing_list


with open('./aoc_day5/aoc_day5.txt') as f:
    data = f.read()
    data = data.split('\n')
    dict_of_positions = {}
    counter = 0
    for rule in data:
        if rule == '':
            break
        counter += 1
        split_rule = rule.split('|')
        pre, post = int(split_rule[0]), int(split_rule[1])
        dict_of_positions[pre] = dict_of_positions.get(pre, []) + [post]

    data = data[counter+1:]
    correct_printing = []
    incorrect_printing = []
    for printing in data:
        printing_list = printing.split(',')
        list_should_be_kept = True
        for i, element in enumerate(printing_list):
            if i == 0 or not dict_of_positions.get(int(element)):
                continue
            
            if int(printing_list[i-1]) in dict_of_positions[int(element)]:
                list_should_be_kept = False
                break
        if list_should_be_kept:
            correct_printing.append(printing_list)
        else:
            incorrect_printing.append(printing_list)

    sum_of_mid = 0
    for printing in incorrect_printing:
        printing = sort_order(dict_of_positions, printing)
        mid = len(printing) // 2
        sum_of_mid += int(printing[mid])
    print(sum_of_mid)

        
    
