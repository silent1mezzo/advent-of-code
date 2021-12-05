numbers = []


def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            numbers.append(line.strip())


def part_1():
    # part 1
    gamma = ''
    epsilon = ''
    positions = [{0: 0, 1: 0}]
    for number in numbers:
        for x, digit in enumerate(number):
            # Expand the array when it finds a new digit
            if x >= len(positions):
                positions.append({0: 0, 1: 0})
            digit = int(digit)
            if digit == 0:
                positions[x][0] += 1
            else:
                positions[x][1] += 1

    for position in positions:
        if position[0] > position[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)


# part 2
def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
