import string, re

GAME = []

def is_symbol(character):
    return character != '.' and not character.isalnum()

def is_part_number(index, start_pos, end_pos):
    is_part_number = False
    symbols = ''
    # CHECK ABOVE
    if index > 0:
        start_range = start_pos - 1 if start_pos > 0 else start_pos
        end_range = end_pos + 2 if end_pos < (len(GAME[index-1])-1) else end_pos
        for x in range(start_range, end_range):
            if is_symbol(GAME[index-1][x]):
                is_part_number = True
                if GAME[index-1][x] == '*':
                    symbols = f'{index-1}-{x}'

    # CHECK SIDES
    if start_pos > 0 and is_symbol(GAME[index][start_pos-1]):
        is_part_number = True
        if GAME[index][start_pos-1] == '*':
            symbols = f'{index}-{start_pos-1}'

    if end_pos < (len(GAME[index])-1) and is_symbol(GAME[index][end_pos+1]):
        is_part_number = True
        if GAME[index][end_pos+1] == '*':
            symbols = f'{index}-{end_pos+1}'
    
    # CHECK BELOW
    if index < len(GAME) - 1:
        start_range = start_pos - 1 if start_pos > 0 else start_pos
        end_range = end_pos + 2 if end_pos < (len(GAME[index+1])-1) else end_pos
        
        for x in range(start_range, end_range):
            if is_symbol(GAME[index+1][x]):
                is_part_number = True
                if GAME[index+1][x] == '*':
                    symbols = f'{index+1}-{x}'

    return is_part_number, symbols

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            GAME.append(line.replace('\n', ''))

def part_1():
    PART_NUMBERS = []
    for index, row in enumerate(GAME):
        for match in re.finditer(r'\d+', row):
            number = int(match.group())
            start_pos = match.start()
            end_pos = match.end()-1

            is_part, symbols = is_part_number(index, start_pos, end_pos)
            if is_part:
                PART_NUMBERS.append(number)

    return sum(PART_NUMBERS)

def part_2():
    RATIOS = {}
    results = 0
    for index, row in enumerate(GAME):
        for match in re.finditer(r'\d+', row):
            number = int(match.group())
            start_pos = match.start()
            end_pos = match.end()-1

            is_part, symbols = is_part_number(index, start_pos, end_pos)
            if symbols:
                if symbols in RATIOS:
                    RATIOS[symbols].append(number)
                else:
                    RATIOS[symbols] = [number]

    for key, item in RATIOS.items():
        if len(item) == 2:
            results += item[0]*item[1]

    return results


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
