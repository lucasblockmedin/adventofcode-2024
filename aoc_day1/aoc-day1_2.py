with open('aoc_day1.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    # remove the last element of the list
    data.pop()
    # create two lists
    list1 = []
    freq_dict = {}
    # iterate through the data
    for line in data:
        line_elements = line.split('   ')
        left, right = line_elements
        list1.append(int(left))
        freq_dict[int(right)] = freq_dict.get(int(right), 0) + 1

distance = 0
for number in list1:
    distance += number * freq_dict.get(number, 0)

print(distance)