def create_dict_of_antennas(data):
    dict_of_antennas = {}
    for i, line in enumerate(data):
        for j, element in enumerate(line):
            if element == '.':
                continue
            else:
                dict_of_antennas[element] = dict_of_antennas.get(element, []) + [(j,i)] # should match (x,y) coordinates
    
    print(dict_of_antennas)            
    return dict_of_antennas

def find_valid_antinodes(list_of_nodes, data):
    n = len(data)
    m = len(data[0])
    # print(f"Bounds of the map: {n}x{m}")
    valid_antinodes_positions = []
    for l, node in enumerate(list_of_nodes):
        for connected_node in list_of_nodes[l+1:]:
            # print(f"\nAnalyzing line between {node} and {connected_node}")
            slope = (connected_node[1] - node[1]) / (connected_node[0] - node[0])
            # line equation
            b = node[1] - slope * node[0]
            # print(f"Line equation: y = {slope}x + {b}")


            for k in range(n):
                intersection = (k - b) / slope
                if abs(intersection - round(intersection)) < 0.0001 and intersection >= 0 and intersection < m:
                    print(f"Intersection at x={intersection} and rounded to {round(intersection)}")
                    intersection = round(intersection)
                    valid_antinodes_positions.append((intersection, k))

    # print(f"Found {len(set(valid_antinodes_positions))} unique antinodes for this frequency")
    return valid_antinodes_positions
    

with open('./aoc_day8/aoc_day8.txt') as f:
    data = f.read()
    data = data.split('\n')
    dict_of_antennas = create_dict_of_antennas(data)
    total_valid_antinodes_positions = []
    for antenna in dict_of_antennas:
        total_valid_antinodes_positions += find_valid_antinodes(dict_of_antennas[antenna], data)
    set_of_valid_antinodes_positions = set(total_valid_antinodes_positions)
    print(len(set_of_valid_antinodes_positions))