import re

with open('./aoc_day3/aoc_day3.txt') as f:
    data = f.read()
    data = data.split('\n')
    matches_row = []
    for row in data:
        matches_row.append(re.findall(r'mul\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\)', row))
    print(matches_row)
    print(len(matches_row))
    result = 0
    for matches in matches_row:
        for match in matches:
            result += int(match[0]) * int(match[1])
    print(result)