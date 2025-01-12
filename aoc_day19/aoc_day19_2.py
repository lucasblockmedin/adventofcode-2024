from functools import lru_cache

def count_combinations(target, base_strings):
    if isinstance(base_strings, list):
        base_strings = tuple(sorted(base_strings))
    
    @lru_cache(maxsize=None)
    def _count_combinations(remaining):
        # Base case: empty string has one way to form it
        if not remaining:
            return 1
            
        # Try each base string as a prefix and sum the counts
        total = 0
        for base in base_strings:
            if remaining.startswith(base):
                total += _count_combinations(remaining[len(base):])
        return total
    
    return _count_combinations(target)

with open('aoc_day19/aoc_day19.txt') as f:
    data = f.read().splitlines()
    print(data)
    base_strings = data.pop(0).split(', ')
    print(base_strings)
    data.pop(0)
    count = 0
    for element in data:
        count += count_combinations(element, base_strings)
    print(count)