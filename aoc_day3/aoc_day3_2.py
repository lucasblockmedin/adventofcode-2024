import re

with open('./aoc_day3/aoc_day3.txt') as f:
    data = f.read()
    data = data.split('\n')
    matches_row = []
    pattern = r'mul\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\)|(don\'t\(\))|(do\(\))'
    for row in data:
        matches_row.append(re.findall(pattern, row))
    result = 0
    should_do = True
    for matches in matches_row:
        for match in matches:
            if match[3] == "do()":
                should_do = True
                continue
            elif match[2] == "don't()":
                should_do = False
                continue
            if should_do and (match[0] != "" and match[1] != ""):
                result += int(match[0]) * int(match[1])
    print(result)