expenses = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            expenses.append(int(line))

def part_1():
    # part 1
    for expense in expenses:
        test = 2020 - expense
        if test in expenses:
            return expense * test



# part 2
def part_2():
    for expense in expenses:
        for e in expenses:
            test = 2020 - expense - e
            if (test in expenses):
                return expense * test * e


read_input()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))