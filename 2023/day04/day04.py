import re
GAMES = {}

def get_game_id(game):
    return int(re.findall(r'\d+', game.split(':')[0])[0])

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            game_id = get_game_id(line)
            results = line.split(':')[1].split('|')
            GAMES[game_id] = [{'winning': re.findall(r'\d+', results[0]), 'numbers': re.findall(r'\d+', results[1])}]

def part_1():
    result = 0
    for id, game in GAMES.items():
        individual_game = game[0]
        number_of_items = len(set(individual_game['winning']) & set(individual_game['numbers']))

        if number_of_items > 0:
            result += 2**(number_of_items-1)

    return result

def part_2():
    result = 0

    for id, game in GAMES.items():
        for individual_game in game:
            number_of_items = len(set(individual_game['winning']) & set(individual_game['numbers']))
            next_id = id + 1
            for x in range(next_id, next_id+number_of_items):
                GAMES[x].append({'winning': GAMES[x][0]['winning'], 'numbers': GAMES[x][0]['numbers']})

    for id, game in GAMES.items():
        result += len(game)

    return result


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
