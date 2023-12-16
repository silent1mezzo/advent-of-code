import re
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append([int(num) for num in line.split()])

def get_value(row, direction):
    if all(x == 0 for x in row):
        return 0
    else:
        diff = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if direction == 'forward':
            return row[-1] + get_value(diff, 'forward')
        elif direction == 'backward':
            return row[0] - get_value(diff, 'backward')

def part_1():
    sum = 0
    for row in data:
        sum += get_value(row, 'forward')

    return sum

def part_2():
    sum = 0
    for row in data:
        sum += get_value(row, 'backward')

    return sum


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
