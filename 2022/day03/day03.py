data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(line)

def part_1():
    sum = 0
    for line in data:
        first, second = line[:len(line)//2], line[len(line)//2:]
        character = ''.join(set(first).intersection(second))
        if character.isupper():
            sum += ord(character) - 38
        else:
            sum += ord(character) - 96
    return sum

def part_2():
    sum = 0
    for i, x in enumerate(data):
        if i % 3 == 0:
            character = ''.join(set(x).intersection(data[i+1]).intersection(data[i+2])).strip()
            if character.isupper():
                sum += ord(character) - 38
            else:
                sum += ord(character) - 96
    return sum


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
