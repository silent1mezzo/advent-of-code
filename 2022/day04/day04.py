data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(line.replace('\n','').split(','))

def part_1():
    total = 0
    for line in data:
        first_range = line[0].split('-')
        second_range = line[1].split('-')
        first = set(range(int(first_range[0]), int(first_range[1])+1))
        second = set(range(int(second_range[0]), int(second_range[1])+1))

        if first.issubset(second) or second.issubset(first):
            total += 1

    return total

def part_2():
    total = 0
    for line in data:
        first_range = line[0].split('-')
        second_range = line[1].split('-')
        first = set(range(int(first_range[0]), int(first_range[1])+1))
        second = set(range(int(second_range[0]), int(second_range[1])+1))

        if not set(first).isdisjoint(second):
            total += 1

    return total



read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
