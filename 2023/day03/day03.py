import string, re

GAME = []

PART_NUMBERS = []
NOT_PART_NUMBERS = []

def is_symbol(character):
    return character != '.' and not character.isalnum()

def is_part_number(index, start_pos, end_pos):
    is_part_number = False
    # CHECK ABOVE
    if index > 0:
        start_range = start_pos - 1 if start_pos > 0 else start_pos
        end_range = end_pos + 2 if end_pos < (len(GAME[index-1])-1) else end_pos
        for x in range(start_range, end_range):
            if is_symbol(GAME[index-1][x]):
                print("FOUND SYMBOL ABOVE", GAME[index-1][x])
                is_part_number = True

    # CHECK SIDES
    if start_pos > 0 and is_symbol(GAME[index][start_pos-1]):
        print("FOUND SYMBOL LEFT SIDE", GAME[index][start_pos-1])
        is_part_number = True

    if end_pos < (len(GAME[index])-1) and is_symbol(GAME[index][end_pos+1]):
        print("FOUND SYMBOL RIGHT SIDE", GAME[index][end_pos+1])
        is_part_number = True
    
    # CHECK BELOW
    if index < len(GAME) - 1:
        start_range = start_pos - 1 if start_pos > 0 else start_pos
        end_range = end_pos + 2 if end_pos < (len(GAME[index+1])-1) else end_pos
        
        for x in range(start_range, end_range):
            if is_symbol(GAME[index+1][x]):
                print("FOUND SYMBOL BELOW", GAME[index+1][x])
                is_part_number = True

    return is_part_number

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            GAME.append(line.replace('\n', ''))

def part_1():
    for index, row in enumerate(GAME):
        for match in re.finditer(r'\d+', row):
            number = int(match.group())
            start_pos = match.start()
            end_pos = match.end()-1

            print("CHECKING NUMBER", number)
            if is_part_number(index, start_pos, end_pos):
                PART_NUMBERS.append(number)
            else:
                NOT_PART_NUMBERS.append(number)

    return sum(PART_NUMBERS)

def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
