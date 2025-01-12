from collections import deque

def compute_price_for_area(data, tracking_matrix, i, j):
    area_type = data[i][j]
    queue = deque([(i, j)])
    num_elements = 0
    perimeter = 0
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
                perimeter += 1
                continue
            # Check if the element is of the same type
            if data[i_][j_] == area_type:
                if tracking_matrix[i_][j_] == 1:
                    continue
                else:
                    tracking_matrix[i_][j_] = 1
                    queue.appendleft((i_, j_))
            else:
                # print('Different type, adding one to the perimeter')
                perimeter += 1
    #     print('Perimeter', perimeter)
    # print('For area type', area_type, 'we have', num_elements, 'elements and', perimeter, 'perimeter')
    return num_elements * perimeter


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
            # pretty_print_matrix(tracking_matrix)
    print(total_price)
            