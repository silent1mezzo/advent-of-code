import operator
data = []

HANDS = {
    'high-card': [],
    'one-pair': [],
    'two-pair': [],
    'threes': [],
    'full-house': [],
    'fours': [],
    'fives': [],
}

def get_type(hand):
    print(hand)
    for character in hand:
        count = hand.count(character)
        if count == 5:
            return 'fives'
        elif count == 4:
            return 'fours'
        elif count == 3:
            hand = hand.replace(character, '')
            if hand.count(hand[0]) == 2:
                return 'full-house'
            else:
                return 'threes'
        elif count == 2:
            hand = hand.replace(character, '')
            if hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2:
                return 'two-pair'
            else:
                return 'one-pair'

    return 'high-card'

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            line = line.replace('\n', '').split(' ')
            hand = line[0]
            bid = line[1]
            hand_type = get_type(hand)
            
            HANDS[hand_type].append({
                'hand': hand,
                'bid': int(bid),
                'rank': None
            })
            sorted_list = sorted(HANDS[hand_type], key=operator.itemgetter('hand'), reverse=True)

def generate_ranks():
    current_rank = 1
    for hand in HANDS:
        if len(HANDS[hand]) == 1:
            HANDS[hand][0]['rank'] = current_rank
            current_rank += 1
        else:
            for x in HANDS[hand]:
                x['rank'] = current_rank
                current_rank += 1

def part_1():
    generate_ranks()
    result = 0
    print(HANDS)
    for hand in HANDS:
        for x in HANDS[hand]:
            result += x['bid'] * x['rank']

    return result

def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
