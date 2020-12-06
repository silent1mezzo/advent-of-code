customs = []

def process_customs():
    with open('input.txt') as reader:
        group = set()
        for line in reader.readlines():
            if line == '\n':
                customs.append(group)
                group = set()
            for char in list(line.strip()):
                group.add(char)

        customs.append(group)


def part_1():
    count = 0
    for custom in customs:
        print len(custom), custom
        count += len(custom)

    return count


process_customs()
print("Answer for part 1: {}".format(part_1()))