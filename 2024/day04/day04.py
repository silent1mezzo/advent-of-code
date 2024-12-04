import re
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(list(line))

def check_forwards(x, y):
    try:
        if "XMAS" in ''.join(data[x][y:y+4]):
            return True
    except:
        pass
    return False

def check_backwards(x, y):
    try:
        if "SAMX" in ''.join(data[x][y-4:y]) and y-4 >= 0:
            return True
    except:
        pass
    return False

def check_down(x, y):
    try:
        string = ''
        for cnt in range(4):
            string += data[x+cnt][y]

        if "XMAS" == string:
            return True
    except:
        pass

    return False

def check_up(x, y):
    try:
        string = ''
        for cnt in range(4):
            if (x-cnt >= 0):
                string += data[x-cnt][y]

        if "XMAS" == string:
            return True
    except:
        pass

    return False

def check_diagonal(x, y):
    found_count = 0
    # Check Up and Right
    try:
        string = ''
        for cnt in range(4):
            if (x-cnt) >= 0 and (y-cnt) >= 0:
                string += data[x-cnt][y-cnt]

        if "XMAS" == string:
            found_count += 1
    except:
        pass


    # Check Up and Left
    try:
        string = ''
        for cnt in range(4):
            if (x-cnt) >= 0:
                string += data[x-cnt][y+cnt]

        if "XMAS" == string:
            found_count += 1
    except:
        pass

     # Check Down and Right
    try:
        string = ''
        for cnt in range(4):
            if (y-cnt) >= 0:
                string += data[x+cnt][y-cnt]

        if "XMAS" == string:
            found_count += 1
    except:
        pass

     # Check Down and Left
    try:
        string = ''
        for cnt in range(4):
            string += data[x+cnt][y+cnt]

        if "XMAS" == string:
            found_count += 1
    except:
        pass

    return found_count


def part_1():
    count = 0
    for x, _ in enumerate(data):
        for y, _ in enumerate(data[x]):
            if check_forwards(x,y):
                count += 1
            
            if check_backwards(x,y):
                count += 1

            if check_down(x,y):
                count += 1

            if check_up(x,y):
                count += 1

            count += check_diagonal(x,y)
    return count

def check_mas(x, y):
    return x != y and x in "MS" and y in "MS"

def part_2():
    count = 0
    for x, _ in enumerate(data):
        for y, _ in enumerate(data[x]):
            if data[x][y] == "A":
                try:
                    if (x-1) >= 0 and (y-1) >= 0:
                        if check_mas(data[x-1][y-1], data[x+1][y+1]) and check_mas(data[x+1][y-1], data[x-1][y+1]):
                            count += 1
                except:
                    pass

    return count


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
