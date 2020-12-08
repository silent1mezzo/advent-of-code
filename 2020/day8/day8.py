lines_of_code = {}
visited_instructions = []

def process_program():
    with open('input.txt') as reader:
        index = 0
        for line in reader.readlines():
            lines_of_code[index] = line.strip()
            index += 1


def part_1():
    accumulator = 0

    index = 0
    while True:
        if index in visited_instructions:
            return accumulator
        
        visited_instructions.append(index)
        
        operation, argument = lines_of_code[index].split(' ')

        if operation == 'acc':
            accumulator += int(argument)
        elif operation == 'jmp':
            index += int(argument)
            continue

        index += 1


process_program()
print("Answer for part 1: {}".format(part_1()))