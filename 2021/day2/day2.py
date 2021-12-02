directions = []


def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            directions.append(line)


def parse_line(line):
    return line.split()


def part_1():
    # part 1
    horizontal = 0
    depth = 0
    for direction in directions:
        direction, unit = parse_line(direction)
        unit = int(unit)
        if direction == "forward":
            horizontal += unit
        elif direction == "down":
            depth += unit
        elif direction == "up":
            depth -= unit

    return horizontal * depth


# part 2
def part_2():
    horizontal = 0
    depth = 0
    aim = 0
    for direction in directions:
        direction, unit = parse_line(direction)
        unit = int(unit)

        if direction == "forward":
            horizontal += unit
            depth += aim * unit
        elif direction == "down":
            aim += unit
        elif direction == "up":
            aim -= unit

    return horizontal * depth


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
