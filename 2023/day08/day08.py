data = {}
instructions = ''

def read_input():
    global instructions
    with open('input.txt') as reader:
        line = reader.readline().strip()
        instructions = line.replace('\n', '')
        for line in reader.readlines():
            line = line.replace('\n', '')
            if line != '':
                parts = line.split('=')
                other = parts[1].replace('(', '').replace(')', '').split(',')
                data[parts[0].strip()] = {
                    'left': other[0].strip(),
                    'right': other[1].strip(),
                }
    print(instructions, data)

def part_1():
    step = 0
    current_index = 'AAA'

    while True:
        for instruction in instructions:
            step +=1
            
            if instruction == 'L':
                current_index = data[current_index]['left']
            else:
                current_index = data[current_index]['right']
        
            if current_index == 'ZZZ':
                return step


def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
