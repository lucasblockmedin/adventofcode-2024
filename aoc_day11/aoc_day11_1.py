def update_data(data):
    new_data = []
    for i, element in enumerate(data):
        if element == '0':
            data[i] = '1'
            new_data.append('1')
        elif len(element) % 2 == 0:
            length = len(element)
            element_left = int(element[:length//2])
            element_right = int(element[length//2:])
            new_data.append(str(element_left))
            new_data.append(str(element_right))
        else:
            data_num = int(element)*2024
            new_data.append(str(data_num))
    return new_data


with open("./aoc_day11/aoc_day11.txt") as f:
    data = f.read()
    data = data.split(' ')
    for blink_nb in range(25):
        print(f"BLINK {blink_nb}")
        data = update_data(data)
    print(len(data))