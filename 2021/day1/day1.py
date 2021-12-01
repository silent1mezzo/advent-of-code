depths = []


def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            depths.append(int(line))


def part_1():
    # part 1
    incr = 0
    prev = None
    for depth in depths:
        if prev and depth > prev:
            incr += 1

        prev = depth

    return incr


# part 2
def part_2():
    incr = 0
    prev = None
    for x, depth in enumerate(depths[2:]):
        # Since we're skipping the first two depths we need to artificially increment the counter
        x += 2

        total = sum([depths[x-2], depths[x-1], depths[x]])
        if prev and total > prev:
            incr += 1

        prev = total

    return incr


read_input()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))
