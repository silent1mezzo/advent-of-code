import re
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(line)

def part_1():
    sum = 0
    for d in data:
        numbers = ''.join(x for x in d if x.isdigit())
        value = int(numbers[0] + numbers[-1])
        sum += value
    return sum

def part_2():
    word_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    sum = 0
    for d in data:
        line_num = []
        for index in range(len(d)):
            if d[index].isdigit():
                line_num.append(d[index])
            else:
                for number, value in word_num.items():
                    if d[index:index+len(number)] == number:
                        line_num.append(value)
        value = int(line_num[0] + line_num[-1])
        sum += value
    return sum
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
