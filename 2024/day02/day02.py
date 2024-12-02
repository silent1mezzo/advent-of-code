import re
import copy
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
            data.append(numbers)

def get_order(x, y):
    if x > y:
        return 'asc'
    elif x < y:
        return 'desc'
    else:
        return 'equal'
    
def safe_change(original_direction, new_direction, x, y):
    if original_direction != new_direction:
        return False
    
    if abs(x - y) < 1 or abs(x - y) > 3:
        return False

    return True

def check_row(direction, row):
    for x, item in enumerate(row):
        try:
            safe = safe_change(direction, get_order(row[x], row[x+1]), row[x], row[x+1])
            if not safe:
                return False, x+1
        except IndexError:
            return True, None

    return safe, None

def part_1():
    safe_rows = 0
    for row in data:
        direction = get_order(row[0], row[1])
        safe = True

        safe, index = check_row(direction, row)
        
        if safe:
            safe_rows += 1

    return safe_rows


def part_2():
    safe_rows = 0
    for row in data:
        direction = get_order(row[0], row[1])
        safe = True

        safe, index = check_row(direction, row)

        if not safe:
            original_row = copy.copy(row)
            row.pop(index)
            safe, index = check_row(direction, row)

            if not safe:
                original_row.pop(index-1)
                direction = get_order(original_row[0], original_row[1])
                safe, index = check_row(direction, original_row)
        
        if safe:
            safe_rows += 1

    return safe_rows

read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
