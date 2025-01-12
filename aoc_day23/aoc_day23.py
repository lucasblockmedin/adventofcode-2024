from collections import defaultdict
import itertools
from tqdm import tqdm


def remove_unordered_duplicates(tuple_list):
    unique_tuples = set(tuple(sorted(t)) for t in tuple_list)
    return [tuple(t) for t in unique_tuples]

def find_three_interconnected(starting_node, nodes):
    interconnected = []
    print('Starting node:', starting_node)
    connected_to_first = nodes[starting_node]
    for node in connected_to_first:
        print('Second Node:', node)
        if node == starting_node:
            continue
        connected_to_second = nodes[node]
        for third_node in connected_to_second:
            print('Third node:', third_node)
            if third_node == node or third_node == starting_node:
                continue
            connected_to_third = nodes[third_node]
            if starting_node in connected_to_third:
                print('Interconnected:', starting_node, node, third_node)
                if starting_node.startswith('t') or node.startswith('t') or third_node.startswith('t'):
                    interconnected.append((starting_node, node, third_node))
    return interconnected

def part1(filename):
    with open(filename, 'r') as file:
        all_interconnected = []
        nodes = defaultdict(list)
        for line in file:
            node, second_node = line.strip().split('-')
            nodes[node] = nodes[node] + [second_node]
            nodes[second_node] = nodes[second_node] + [node]
        print(nodes)
        for node in nodes:
            interconnected = find_three_interconnected(node, nodes)
            all_interconnected.extend(interconnected)
        all_interconnected = remove_unordered_duplicates(all_interconnected)
        print(all_interconnected)
        print(len(all_interconnected))

# def is_fully_connected(nodes_set, adjacency):
#     for node in nodes_set:
#         for other_node in nodes_set:
#             if node != other_node and other_node not in adjacency[node]:
#                 return False
#     return True

# def find_largest_interconnected_set(nodes):
#     all_nodes = set(nodes.keys())
    
#     for size in tqdm(range(len(all_nodes), 1, -1), desc="Checking sizes"):
#         combinations = list(itertools.combinations(all_nodes, size))
#         for combo in tqdm(combinations, desc=f"Checking combinations of size {size}", leave=False):
#             if is_fully_connected(combo, nodes):
#                 print(f"Found fully connected set of size {size}: {combo}")
#                 return combo
    
#     return None

def find_max_clique(nodes):
    def get_neighbors(node):
        return set(nodes[node])
    
    max_clique = set()
    
    def choose_pivot(P, X):
        # Choose the vertex from P union X that has the most connections to P
        # This helps eliminate branches that won't lead to maximum cliques
        # print('P:', P)
        # print('X:', X)
        union = P.union(X)
        # print('Union:', union)
        if not union:
            return None
        return max(union, key=lambda u: len(P.intersection(get_neighbors(u))))
    
    def bron_kerbosch(R, P, X):
        nonlocal max_clique
        
        if not P and not X:
            if len(R) > len(max_clique):
                max_clique = R.copy()
            return
        
        pivot = choose_pivot(P, X)
        # print('Pivot:', pivot)
        if pivot is None:
            return
            
        P_copy = P.copy()
        
        # For each vertex not connected to the pivot
        for v in P.difference(get_neighbors(pivot)):
            # print('V:', v)
            neighbors_v = get_neighbors(v)
            bron_kerbosch(
                R.union({v}),                    # Add vertex to clique
                P_copy.intersection(neighbors_v), # Only neighbors that are in P
                X.intersection(neighbors_v)       # Only neighbors that are in X
            )
            print('Max clique:', max_clique)
            P_copy.remove(v)   # Remove processed vertex from P
            X.add(v)          # Add processed vertex to X
    
    # Initial call with all vertices in P
    all_vertices = set(nodes.keys())
    bron_kerbosch(set(), all_vertices, set())
    
    return max_clique

def part2(filename):
    nodes = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            node, second_node = line.strip().split('-')
            nodes[node].append(second_node)
            nodes[second_node].append(node)
    
    largest_set = find_max_clique(nodes)
    print(f"Largest fully connected set: {largest_set}")
    print(f"Size: {len(largest_set)}")
    sorted_set = sorted(largest_set)
    print(','.join(sorted_set))

if __name__ == '__main__':
    # part1('aoc_day23/aoc_day23.txt')
    part2('aoc_day23/aoc_day23_test.txt')
        
                    