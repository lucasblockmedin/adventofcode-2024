def find_next_empty_memory(memory_list):
    idx = 0
    found_empty = False
    while not found_empty:
        # print(f'Evaluating index {idx} of memory_list {memory_list}')
        if idx >= len(memory_list)-1:
            return -1
        current_element = memory_list[idx]
        if current_element is None:
            return idx
        idx += 1

with open('./aoc_day9/aoc_day9.txt') as f:
    data = f.read()
    # print(data)
    memory_list = []
    total_empty_memory = 0
    first_empty_memory = int(data[0])
    for i, number in enumerate(data):
        # print(i, number)
        if i % 2 == 0:
            # print('even')
            for k in range(int(number)):
                memory_list.append(i//2)
            
        else:
            # print('odd')
            for k in range(int(number)):
                memory_list.append(None)
                total_empty_memory += 1
    
    # print(memory_list)
    # print(total_empty_memory)
    # print(first_empty_memory)
    while total_empty_memory > 0:
        last_element = memory_list.pop()
        # print(f'MEMORY LIST {memory_list}')
        if last_element is None:
            total_empty_memory -= 1
        else:
            memory_list[first_empty_memory] = last_element
            total_empty_memory -= 1
        next_empty_memory = find_next_empty_memory(memory_list[first_empty_memory:])
        if first_empty_memory == -1:
            # print('there is no more memory available?')
            break
        else:
            first_empty_memory += next_empty_memory

    # print(memory_list)
    checksum = 0
    for i, element in enumerate(memory_list):
        checksum += i*int(element)
    print(checksum)
            