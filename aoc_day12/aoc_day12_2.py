from collections import deque

def compute_number_of_sides(area, n, m):
    # We need to count sides only once, so we take our area, and look into the sides that can be created
    # This is kind of the same as looking for corners
    corners = 0
    for i, j in area:
        over = (i-1, j)
        left = (i, j-1)
        right = (i, j+1)
        under = (i+1, j)
        under_left = (i+1, j-1)
        under_right = (i+1, j+1)
        if over not in area and left not in area:
            corners += 1
        if under not in area and left not in area:
            corners += 1
        if over not in area and right not in area:
            corners += 1
        if under not in area and right not in area:
            corners += 1
        if left not in area and (under in area and under_left in area):
            corners += 1
        if right not in area and (under in area and under_right in area):
            corners += 1
        if under not in area and (right in area and under_right in area):
            corners += 1
        if under not in area and (left in area and under_left in area):
            corners += 1

    return corners


def compute_price_for_area(data, tracking_matrix, i, j):
    area_type = data[i][j]
    queue = deque([(i, j)])
    list_of_area_elements = [(i, j)]
    num_elements = 0
    while queue:
        # Recover the element coordinates
        i, j = queue.pop()
        # print('Element', i, j)
        # Set element as checked
        tracking_matrix[i][j] = 1
        num_elements += 1
        # Look into all elements up, down, left and right
        for i_, j_ in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            # Check if the element is in the boundaries
            if i_ < 0 or i_ >= len(data) or j_ < 0 or j_ >= len(data[0]):
                # print('Out of boundaries, adding one to the perimeter')
                continue
            # Check if the element is of the same type
            if data[i_][j_] == area_type:
                if tracking_matrix[i_][j_] == 1:
                    continue
                else:
                    tracking_matrix[i_][j_] = 1
                    queue.appendleft((i_, j_))
                    list_of_area_elements.append((i_, j_))
    #     print('Perimeter', perimeter)
    # print('For area type', area_type, 'we have', num_elements, 'elements and', perimeter, 'perimeter')
    print(list_of_area_elements)
    print(sorted(list_of_area_elements))

    nb_sides = compute_number_of_sides(list_of_area_elements, len(tracking_matrix), len(tracking_matrix[0]))
    print('NB sides : ', nb_sides)
    return num_elements * nb_sides


def pretty_print_matrix(matrix):
    for row in matrix:
        print(row)

with open("./aoc_day12/aoc_day12.txt") as f:
    data = f.read().strip().split('\n')
    print(data)
    n = len(data)
    m = len(data[0])
    # pretty_print_matrix(data)
    tracking_matrix = [[0 for _ in range(m)] for _ in range(n)]
    total_price = 0
    for i in range(n):
        for j in range(m):
            if tracking_matrix[i][j] == 1:
                continue
            total_price += compute_price_for_area(data, tracking_matrix, i, j)
            pretty_print_matrix(tracking_matrix)
    print(total_price)