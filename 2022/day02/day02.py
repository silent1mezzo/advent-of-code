MOVES = []

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

SCORES = {
    PAPER: 2,
    ROCK: 1,
    SCISSORS: 3,
    'LOSE': 0,
    'DRAW': 3,
    'WIN': 6
}

def calculate_outcome(their_move, your_move)
    if their_move == your_move:
        return 'DRAW'
    elif (their_move == ROCK && your_move=PAPER) || (their_move == PAPER && your_move=SCISSORS) || (their_move == SCISSORS && your_move=ROCK)  
        return 'WIN'
    return 'LOSE'

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            moves = line.split(' ')
            your_move = ROCK if moves[1] == 'X' elif PAPER if moves[1] == 'Y' else SCISSORS,
            MOVES = {
                'theirs': moves[0],
                'yours': your_move,
                'outcome': calculate_outcome(moves[0], your_move)
            }

def part_1():
    print(MOVES)
    pass

def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
