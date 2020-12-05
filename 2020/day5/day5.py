LOW_CHARS = ['F', 'L']
seat_ids = []

def process_seats():
    with open('input.txt') as reader:
        for line in reader.readlines():
            seat = line.strip()
            seat_row = seat_search(seat[:7], 0, 0, 127)
            seat_col = seat_search(seat[7:10], 0, 0, 7)
            seat_ids.append(seat_row * 8 + seat_col)

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
    return max(seat_ids)

def part_2():
    # Sum up all of the seat IDs from the lowest one to the highest one.
    expected_total = sum(range(min(seat_ids), max(seat_ids)+1))
    
    # Sum up the IDs from the seats we've generated
    total = sum([seat for seat in seat_ids])

    return expected_total - total



process_seats()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))