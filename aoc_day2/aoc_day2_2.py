def report_is_safe(report):
    for i, levels in enumerate(report):
        if i == 0:
            current_diff = 0
            continue
        current_diff = int(levels) - int(report[i - 1])
        if abs(current_diff) < 1 or abs(current_diff) > 3:
            return False, i
        if i == 1:
            sign = current_diff // abs(current_diff)
            continue
        else:
            prev_sign = sign
            sign = current_diff // abs(current_diff) 
        if prev_sign != sign:
            return False, i
    return True, None

with open('./aoc_day2/aoc_day2_maria.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()
    num_safe_reports = 0
    for report in data:
        report = report.split(' ')
        report_safety, index = report_is_safe(report)
        if not report_safety:
            report_safety_left, _ = report_is_safe(report[:index-1] + report[index:])
            report_safety_curr, _ = report_is_safe(report[:index] + report[index + 1:])
            report_safety_right, _ = report_is_safe(report[:index] + report[index + 1:])
            if not report_safety_left and not report_safety_left and not report_safety_right:
                # Test if removing the first element makes the report safe
                report_safety, _ = report_is_safe(report[1:])
                if not report_safety:
                    print('Not safe')
                    continue
        num_safe_reports += 1

    print(num_safe_reports)

