def create_dict_of_antennas(data):
    dict_of_antennas = {}
    for i, line in enumerate(data):
        for j, element in enumerate(line):
            if element == '.':
                continue
            else:
                dict_of_antennas[element] = dict_of_antennas.get(element, []) + [(i,j)]
    
    print(dict_of_antennas)            
    return dict_of_antennas

def find_valid_antinodes(list_of_nodes, data):
    n = len(data)
    m = len(data[0])
    print(f"Bounds of the map: {n}x{m}")
    valid_antinodes_positions = []
    for l, node in enumerate(list_of_nodes):
        for connected_node in list_of_nodes[l+1:]:
            vector = [connected_node[0] - node[0], connected_node[1] - node[1]]
            if node[0] - vector[0] < 0 or node[0] - vector[0] >= n or node[1] - vector[1] < 0 or node[1] - vector[1] >= m:
                print(f"Node is out of bounds")
                print(f"New coordinates: {node[0] - vector[0], node[1] - vector[1]}")
            else:
                print(f"Node is in bounds")
                print(f"New coordinates: {node[0] - vector[0], node[1] - vector[1]}")
                valid_antinodes_positions.append((node[0] - vector[0], node[1] - vector[1]))
            
            if connected_node[0] + vector[0] < 0 or connected_node[0] + vector[0] >= n or connected_node[1] + vector[1] < 0 or connected_node[1] + vector[1] >= m:
                print(f"Connected node is out of bounds")
                print(f"New coordinates: {connected_node[0] + vector[0], connected_node[1] + vector[1]}")
            else:
                print(f"Connected node is in bounds")
                print(f"New coordinates: {connected_node[0] + vector[0], connected_node[1] + vector[1]}")
                valid_antinodes_positions.append((connected_node[0] + vector[0], connected_node[1] + vector[1]))

    return valid_antinodes_positions

        


    

with open('./aoc_day8/aoc_day8_test.txt') as f:
    data = f.read()
    data = data.split('\n')
    print(data)
    dict_of_antennas = create_dict_of_antennas(data)
    total_valid_antinodes_positions = []
    for antenna in dict_of_antennas:
        total_valid_antinodes_positions += find_valid_antinodes(dict_of_antennas[antenna], data)
    print(total_valid_antinodes_positions)
    set_of_valid_antinodes_positions = set(total_valid_antinodes_positions)
    print(len(set_of_valid_antinodes_positions))
    