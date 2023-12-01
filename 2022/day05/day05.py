import re
import copy
data = {}
instructions = []


def read_input():
    row_cnt = 0
    num_columns = 0
    reading_columns = True
    with open('input.txt') as reader:
        for line in reader.readlines():
            if reading_columns:
                if row_cnt == 0:
                    num_columns = int(len(line) / 4 + 1)
                    for x in range(1, num_columns):
                        data[x] = []
                row_cnt += 1

                if line.strip()[0].isdigit():
                    reading_columns = False
                else:
                    for i, x in enumerate(line):
                        if i % 4 == 0 and line[i+1].isalpha():
                            data[int(i / 4) + 1].append(line[i+1])

            if 'move' in line:
                instr = re.findall(r'\d+', line)
                instructions.append({'number': int(instr[0]), 'from': int(instr[1]), 'to': int(instr[2])})

def part_1():
    data1 = copy.deepcopy(data)
    result = ''
    for instruction in instructions:
        for x in range(instruction['number']):
            data1[instruction['to']].insert(0, data1[instruction['from']].pop(0))

    for element in data1:
        result += data[element][0]

    return result

    

def part_2():
    data2 = copy.deepcopy(data)
    result = ''

    for instruction in instructions:
        items = data2[instruction['from']][:instruction['number']]
        items.reverse()
        for item in items:
            data2[instruction['to']].insert(0, item)

        data2[instruction['from']] = data2[instruction['from']][instruction['number']:]

    for element in data2:
        if data2[element]:
            result += data2[element][0]

    return result



read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
