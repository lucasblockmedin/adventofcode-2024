with open('./aoc_day2/aoc_day2.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()
    num_safe_reports = 0
    for report in data:
        report = report.split(' ')
        print(report)
        safe = True
        for i, levels in enumerate(report):
            if i == 0:
                current_diff = 0
                continue
            current_diff = int(levels) - int(report[i - 1])
            if abs(current_diff) < 1 or abs(current_diff) > 3:
                print('Not safe, too big of a difference')
                safe = False
                break
            if i == 1:
                sign = current_diff // abs(current_diff)
                continue
            else:
                prev_sign = sign
                sign = current_diff // abs(current_diff) 
            if prev_sign != sign:
                safe = False
                print('Not safe, change of sign')
                break
        if safe:
            print('Safe report')
            num_safe_reports += 1
    print(num_safe_reports)