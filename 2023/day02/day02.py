import re
data = []

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

LIMITS = {
    RED: 12,
    GREEN: 13,
    BLUE: 14
}

RESULTS = {}

def get_game_id(game):
    return int(re.findall(r'\d+', game.split(':')[0])[0])

def get_round_data(rounds):
    MAX_BLUE = 0
    MAX_RED = 0
    MAX_GREEN = 0
    for round in rounds:
        values = round.split(',')
        for value in values:
            if BLUE in value:
                blue = int(re.findall(r'\d+', value)[0])
                if blue > MAX_BLUE:
                    MAX_BLUE = blue
            elif RED in value:
                red = int(re.findall(r'\d+', value)[0])
                if red > MAX_RED:
                    MAX_RED = red
            elif GREEN in value:
                green = int(re.findall(r'\d+', value)[0])
                if green > MAX_GREEN:
                    MAX_GREEN = green

    return {RED: MAX_RED, BLUE: MAX_BLUE, GREEN: MAX_GREEN}

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            game_id = get_game_id(line)
            RESULTS[game_id] = get_round_data(line.split(':')[1:][0].split(';'))

def part_1():
    game_sum = 0
    for id, game in RESULTS.items():
        if game[RED] <= LIMITS[RED] and game[GREEN] <= LIMITS[GREEN] and game[BLUE] <= LIMITS[BLUE]:
            game_sum += id

    return game_sum

def part_2():
    game_sum = 0
    for id, game in RESULTS.items():
        game_sum += game[RED] * game[GREEN] * game[BLUE]

    return game_sum


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
