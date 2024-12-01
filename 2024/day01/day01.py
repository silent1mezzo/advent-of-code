data = []

left_list = []
right_list = []
def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            pairs = line.split()
            left_list.append(int(pairs[0]))
            right_list.append(int(pairs[1]))

def part_1():
    diff = 0
    left_list.sort()
    right_list.sort()
    for x, _ in enumerate(left_list):
        diff += abs(right_list[x] - left_list[x])

    return diff

def part_2():
    diff = 0
    for item in left_list:
        diff += item * right_list.count(item)

    return diff


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
