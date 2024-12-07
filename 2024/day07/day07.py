import re
from itertools import product
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            result = line.split(':')
            rest = [int(s) for s in re.findall(r'\d+', result[1])]
            data.append([int(result[0]), rest])

def check_true(numbers, operators):
    result = numbers[0]

    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))

    return result

def part_1():
    total = 0
    for test_value, numbers in data:
        n = len(numbers)
        if n == 1:
            total += test_value
            break

        operator_combinations = product("+*", repeat=n - 1)

        for ops in operator_combinations:
            if check_true(numbers, ops) == test_value:
                total += test_value
                break

    return total


def part_2():
    total = 0
    for test_value, numbers in data:
        n = len(numbers)
        if n == 1:
            total += test_value
            break

        operator_combinations = product("+*|", repeat=n - 1)

        for ops in operator_combinations:
            formatted_ops = [op if op != '|' else '||' for op in ops]
            if check_true(numbers, formatted_ops) == test_value:
                total += test_value
                break

    return total


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
