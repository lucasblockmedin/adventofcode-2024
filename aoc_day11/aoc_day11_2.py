from functools import lru_cache

@lru_cache(maxsize=None)
def get_sequence_length(element: str, steps: int) -> int:
    """
    Instead of storing all elements, just calculate the final length.
    """
    if steps == 0:
        return 1
        
    if element == '0':
        return get_sequence_length('1', steps - 1)
    elif len(element) % 2 == 0:
        length = len(element)
        left = str(int(element[:length//2]))
        right = str(int(element[length//2:]))
        return get_sequence_length(left, steps - 1) + get_sequence_length(right, steps - 1)
    else:
        new_val = str(int(element) * 2024)
        return get_sequence_length(new_val, steps - 1)

# Main processing
with open("./aoc_day11/aoc_day11.txt") as f:
    data = f.read().strip().split()
    count = 0
    for element in data:
        print(element)
        count += get_sequence_length(element, 75)
    print(count)