jolts = []
def process_jolts():
    with open('input.txt') as reader:
        count = 0
        for line in reader.readlines():
            jolts.append(int(line.strip()))

def part_1():
    len_one = []
    len_three = []

    sorted_jolts = sorted(jolts)

    # Process the first element
    diff = sorted_jolts[0] - 0
    if diff == 1:
        len_one.append(sorted_jolts[0])
    elif diff == 3:
        len_three.append(sorted_jolts[0])

    for i, jolt in enumerate(sorted_jolts):
        if len(sorted_jolts) == i+1:
            len_three.append(jolt)
            continue

        diff = sorted_jolts[i+1] - jolt
        if diff == 1:
            len_one.append(jolt)
        elif diff == 3:
            len_three.append(jolt)
    
    return len(len_one) * len(len_three)

process_jolts()
print("Answer for part 1: {}".format(part_1()))
