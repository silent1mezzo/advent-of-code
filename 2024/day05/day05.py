import re
rules = {}
pages = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            if '|' in line:
                rule = line.split('|')
                first = int(rule[0])
                second = int(rule[1])
                if second in rules:
                    rules[second].append(first)
                else:
                    rules[second] = [first]
            elif ',' in line:
                pages.append([int(s) for s in re.findall(r'\d+', line)])

def get_middle(l):
    index = int((len(l) - 1)/2)
    return l[index]


def part_1():
    result = 0
    valid_lists = []
    for page in pages:
        valid = True

        for x, number in enumerate(page):
            if not valid:
                break
            if number not in rules:
                continue

            # Make sure all numbers are either before it or not there
            for rule in rules[number]:
                if rule not in page or rule in page[:x]:
                    valid = True
                else:
                    valid = False
                    break
        
        if valid:
            valid_lists.append(page)

    for list in valid_lists:
        result += get_middle(list)

    return result
            
            

def part_2():
    result = 0
    for rule in rules:
        print(f"{rule}:{rules[rule]}")
    invalid_lists = []
    for page in pages:
        valid = True
        previously_fixed = False
        while True:
            fixed = False
            for x in range(len(page)):
                number = page[x]
                print(f"Processing page {page}")
                print(f"Processing element {number} at {x} ")
                if number not in rules:
                    print(f"{number} not found in rules, continuing")
                    continue

                # Make sure all numbers are either before it or not there
                for rule in rules[number]:
                    if rule not in page or rule in page[:x]:
                        pass
                    else:
                        print(f"{rule} violated, putting it at {x}")
                        page.remove(rule)
                        page.insert(x, rule)
                        previously_fixed = True
                        fixed = True
                        break
            
            if not fixed:
                print(f"Processed {page} fully, was previously fixed? {previously_fixed}")
                if previously_fixed:
                    invalid_lists.append(page)
                break
    
        
    
    print(f"Invalid Lists: {invalid_lists}")
    for list in invalid_lists:
        result += get_middle(list)
    
    return result


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
