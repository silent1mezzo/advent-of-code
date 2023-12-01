MOVES_PART1 = []
MOVES_PART2 = []

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

SCORES = {
    PAPER: 2,
    ROCK: 1,
    SCISSORS: 3,
    'LOSE': 0,
    'DRAW': 3,
    'WIN': 6
}

def calculate_outcome(their_move, your_move):
    if their_move == your_move:
        return 'DRAW'
    elif (their_move == ROCK and your_move == PAPER) or (their_move == PAPER and your_move == SCISSORS) or (their_move == SCISSORS and your_move == ROCK):
        return 'WIN'
    return 'LOSE'

def calculate_move(their_move, outcome):
    if outcome == LOSE:
        if their_move == ROCK:
            return SCISSORS, 'LOSE'
        elif their_move == PAPER:
            return ROCK, 'LOSE'
        elif their_move == SCISSORS:
            return PAPER, 'LOSE'
    elif outcome == WIN:
        if their_move == ROCK:
            return PAPER, 'WIN'
        elif their_move == PAPER:
            return SCISSORS, 'WIN'
        elif their_move == SCISSORS:
            return ROCK, 'WIN'

    return their_move, 'DRAW'

def convert(move):
    if move == 'X':
        return ROCK
    elif move == 'Y':
        return  PAPER
    return SCISSORS

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            moves = line.replace('\n', '').split(' ')
            your_move = convert(moves[1])
            MOVES_PART1.append({
                'theirs': moves[0],
                'yours': your_move,
                'outcome': calculate_outcome(moves[0], your_move)
            })
            
            your_move = calculate_move(moves[0], moves[1])
            MOVES_PART2.append({
                'theirs': moves[0],
                'yours': your_move[0],
                'outcome': your_move[1]
            })

def part_1():
    sum = 0
    for move in MOVES_PART1:
        sum += SCORES[move['yours']] + SCORES[move['outcome']]

    return sum

def part_2():
    sum = 0
    for move in MOVES_PART2:
       sum += SCORES[move['yours']] + SCORES[move['outcome']]

    return sum 


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
