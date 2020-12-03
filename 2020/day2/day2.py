passwords = []
def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            passwords.append(line)

def parse_string(row):
    parts = row.split(' ')
    num = parts[0].split('-')
    return(int(num[0]), int(num[1]), parts[1].strip(':'), parts[2])

def part_1():
    correct_passwords = 0
    for line in passwords:
        min_count, max_count, letter, password = parse_string(line)
        occurrences = password.count(letter)

        if occurrences >= min_count and occurrences <= max_count:
            correct_passwords += 1

    return correct_passwords

def part_2():
    correct_passwords = 0
    for line in passwords:
        min_count, max_count, letter, password = parse_string(line)
        occurrences = password.count(letter)
        
        valid = 0
        if password[min_count-1] == letter:
            valid += 1 

        if password[max_count-1] == letter:
            valid +=1 
        
        if valid == 1:
            correct_passwords += 1

    return correct_passwords


read_input()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))