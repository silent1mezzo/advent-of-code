import re

TIMES = []
DISTANCES = []
def read_input():
    with open('input.txt') as reader:
        TIMES.extend(re.findall(r'\d+', reader.readline()))
        DISTANCES.extend(re.findall(r'\d+', reader.readline()))

def part_1():
    result = 0
    for index, time in enumerate(TIMES):
        speed = 0
        max_time = int(time)
        wins = 0
        for x in range(max_time):
            speed = x
            time_left = max_time - x
            distance = speed * time_left

            if distance > int(DISTANCES[index]):
                wins += 1

        if result == 0:
            result = wins
        else:
            result *= wins

    return result


def part_2():
    TIME = int(''.join(TIMES))
    DISTANCE = int(''.join(DISTANCES))
    
    result = 0
    speed = 0
    wins = 0
    for x in range(TIME):
        speed = x
        time_left = TIME - x
        distance = speed * time_left
        if distance > DISTANCE:
            wins += 1

    if result == 0:
        result = wins
    else:
        result *= wins

    return result

read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
