import re
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL_FIELDS = ['cid']

passports = []
def process_passports():
    with open('input.txt') as reader:
        passport = {}
        for line in reader.readlines():
            # Blank new line, flush passport to passports
            if line == '\n':
                passports.append(passport)
                passport = {}
                continue
            
            # Split line into parts
            parts = line.rstrip().split(' ')
            for part in parts:
                key, value = part.split(':')
        
                passport[key] = value

        # flush the last passport
        passports.append(passport)

def check_passport(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    BYR_CHECK = int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    IYR_CHECK = int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    EYR_CHECK = len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

    '''hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    '''
    HGT_CHECK = False
    hgt_pattern = re.match(r"([0-9]+)([a-z]+)", passport['hgt'], re.I)
    if hgt_pattern:
        items = hgt_pattern.groups()
        
        if items[1] == 'cm':
            HGT_CHECK = int(items[0]) >= 150 and int(items[0]) <= 193
        else:
            HGT_CHECK = int(items[0]) >= 59 and int(items[0]) <= 76


    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl_pattern = re.compile("^#[0-9a-f]{6}$")
    HCL_CHECK = bool(hcl_pattern.match(passport['hcl']))

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    VALID_ECL = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ECL_CHECK = passport['ecl'] in VALID_ECL

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_pattern = re.compile("^[0-9]{9}$")
    PID_CHECK = bool(pid_pattern.match(passport['pid']))

    return all([BYR_CHECK, IYR_CHECK, EYR_CHECK, HGT_CHECK, HCL_CHECK, ECL_CHECK, PID_CHECK])


def part_1():
    valid_passports = 0 
    for passport in passports:
        if all([key in passport.keys() for key in REQUIRED_FIELDS]):
            valid_passports += 1

    return valid_passports

def part_2():
    valid_passports = 0 
    for passport in passports:
        if all([key in passport.keys() for key in REQUIRED_FIELDS]) and check_passport(passport):
            valid_passports += 1

    return valid_passports

process_passports()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))