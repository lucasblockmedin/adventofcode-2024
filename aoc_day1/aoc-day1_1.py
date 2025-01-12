with open('aoc_day1_maria.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    # remove the last element of the list
    data.pop()
    # create two lists
    list1_sum = 0
    list1 = []
    list2_sum = 0
    list2 = []
    # iterate through the data
    for i in data:
        # split the data into a list
        i = i.split('   ')
        list1_sum += int(i[0])
        list1.append(int(i[0]))
        list2_sum += int(i[1])
        list2.append(int(i[1]))
    f.close()

list_1_sum_b = sum(list1)
list_2_sum_b = sum(list2)

list_1_sorted = sorted(list1)
list_2_sorted = sorted(list2)

diff = 0
for a, b in zip(list_1_sorted, list_2_sorted):
    print(a, b)
    diff += abs(a - b)

print(diff)
# print(list1_sum, list_1_sum_b)
# print(list2_sum, list_2_sum_b)

# print(f"Difference using option 1: {list1_sum - list2_sum}")
# print(f"Difference using option 2: {list_1_sum_b - list_2_sum_b}")