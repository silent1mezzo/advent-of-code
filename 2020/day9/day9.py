from itertools import combinations

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


print("Answer for part 1: {}".format(part_1()))