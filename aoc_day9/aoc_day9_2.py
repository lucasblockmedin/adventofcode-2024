with open('./aoc_day9/aoc_day9.txt') as f:
    data = f.read()
    # print(data)
    memory_list = []
    list_of_missing = []
    list_of_files = []
    total_empty_memory = 0
    first_empty_memory = int(data[0])
    idx_in_list = 0
    for i, number in enumerate(data):
        # print(i, number)
        if i % 2 == 0:
            # print('even')
            list_of_files.append((i//2, int(number), idx_in_list, idx_in_list+int(number)))
            idx_in_list += int(number)
            for k in range(int(number)):
                memory_list.append(i//2)
            
        else:
            # print('odd')
            list_of_missing.append((idx_in_list, idx_in_list+int(number)))
            idx_in_list += int(number)
            for k in range(int(number)):
                memory_list.append(None)
                total_empty_memory += 1
    list_of_files.reverse()
    print(memory_list)
    # print(total_empty_memory)
    # print(first_empty_memory)
    # print(list_of_missing)
    # print(list_of_files)
    for file in list_of_files:
        value, size, val_left_idx, val_right_idx = file
        # Look through all empty spaces for leftmost valid position
        best_position = None
        best_space_idx = None
        
        for space_idx, (left_idx, right_idx) in enumerate(list_of_missing):
            if right_idx - left_idx >= size and left_idx < val_left_idx:  # If space is big enough and to the left
                best_position = left_idx
                best_space_idx = space_idx
                break  # Take first (leftmost) valid space we find
                
        if best_position is not None:
            # Move the file
            for i in range(size):
                memory_list[best_position + i] = value
                memory_list[val_left_idx + i] = None
                
            # Update the empty spaces
            left_idx, right_idx = list_of_missing[best_space_idx]
            if right_idx - left_idx == size:
                list_of_missing.pop(best_space_idx)
            else:
                list_of_missing[best_space_idx] = (left_idx + size, right_idx)
            
            list_of_missing.append((val_left_idx, val_right_idx))

    print(memory_list)
    checksum = 0
    for idx, element in enumerate(memory_list):
        if element is None:
            continue
        else:
            checksum += idx*element
    print(checksum)



            