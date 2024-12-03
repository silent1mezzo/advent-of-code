import re
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(line)


def part_1():
    result = 0
    for line in data:
        groups = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
        for group in groups:
            first, second = re.findall(r'\d+', group)
            result += int(first) * int(second)

    return result

def part_2():
    result = 0
    process = True
    for line in data:
        groups = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)', line)
        for group in groups:
            if group == "do()":
                process = True
            elif group == "don't()":
                process = False
            else:
                if process:
                    first, second = re.findall(r'\d+', group)
                    result += int(first) * int(second)

    return result



read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
