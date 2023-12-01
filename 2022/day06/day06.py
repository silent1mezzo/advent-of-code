import operator

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data = line
    return data

def is_unique(string):
    for i in string:
        if operator.countOf(string, i) > 1:
            return False
    return True

def solution(offset):
    data = read_input()
    for index, character in enumerate(data):
        if is_unique(data[index:index+offset]):
            return index+offset

read_input()
print(f"Answer for part 1: {solution(4)}")
print(f"Answer for part 2: {solution(14)}")
