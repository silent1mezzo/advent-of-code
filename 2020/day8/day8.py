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


def part_2():
    # Loop through every iteration, we're brute forcing it folks
    for i in range(len(lines_of_code)):
        local_copy = lines_of_code.copy()

        # Reset Everything
        accumulator = 0
        index = 0
        visited_instructions = []

        operation, argument = local_copy[i].split(' ')
        if operation == 'jmp':
            local_copy[i] = 'nop {}'.format(argument)
        elif operation == 'nop':
            local_copy[i] = 'jmp {}'.format(argument)

        while True:
            if index in visited_instructions:
                break

            if index == len(local_copy):
                return accumulator
            
            visited_instructions.append(index)
            
            operation, argument = local_copy[index].split(' ')

            if operation == 'acc':
                accumulator += int(argument)
            elif operation == 'jmp':
                index += int(argument)
                continue    

            index += 1

process_program()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))