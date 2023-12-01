import re
data = []

def read_input():
    with open('input.txt') as reader:
        sum = 0
        for line in reader.readlines():
            if line != '\n':
                sum += int(line)
            else:
                data.append(sum)
                sum = 0
        # end of file summation
        data.append(sum)
    
def part_1():
    return max(data)

def part_2():
    return sum(sorted(data)[-3:])


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
