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

            
def part_1():
    valid_passports = 0 
    for passport in passports:
        if all([key in passport.keys() for key in REQUIRED_FIELDS]):
            valid_passports += 1

    return valid_passports

process_passports()
print("Answer for part 1: {}".format(part_1()))