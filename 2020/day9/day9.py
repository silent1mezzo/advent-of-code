from itertools import accumulate, combinations

PREAMBLE = 25
data = [None] * PREAMBLE

def part_1():
    with open('input.txt') as reader:
        count = 0
        for line in reader.readlines():
            current_data = int(line.strip())
            if count >= PREAMBLE:
                VALID = False
                for pairs in combinations(data, 2):
                    if sum(pairs) == current_data:
                        VALID = True
                    
                if VALID == False:
                    return current_data

            data[count % PREAMBLE] = int(line.strip())
            count += 1

def part_2():
    INVALID_NUM = part_1()

    with open('input.txt') as reader:
        count = 0
        for line in reader.readlines():
            if count >= PREAMBLE:
                VALID = False
                for idx, d in enumerate(accumulate(data)):
                    if d == INVALID_NUM:
                        return min(data[:idx]) + max(data[:idx])

            data[count % PREAMBLE] = int(line.strip())
            count += 1


#rint("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))