SEATS = []
LOW_CHARS = ['F', 'L']

def process_seats():
    with open('input.txt') as reader:
        for line in reader.readlines():
            SEATS.append(line.strip())

def seat_search(seat, array_idx, low=0, high=127):
    mid = (high + low) // 2
    char = seat[array_idx]
    
    if array_idx+1 == len(seat):
        if char in LOW_CHARS:
            return low
        else:
            return mid+1

    if char in LOW_CHARS:
        return seat_search(seat, array_idx+1, low, mid)
    else:
        return seat_search(seat, array_idx+1, mid+1, high)


def part_1():
    max_seat = 0
    for seat in SEATS:
        seat_row = seat_search(seat[:7], 0, 0, 127)
        seat_col = seat_search(seat[7:10], 0, 0, 7)
        seat_id = seat_row * 8 + seat_col
        if seat_id > max_seat:
            max_seat = seat_id

    return max_seat


process_seats()
print("Answer for part 1: {}".format(part_1()))