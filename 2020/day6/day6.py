customs = []
passenger_count = []
def process_customs():
    with open('input.txt') as reader:
        group = []
        num_passengers = 0
        for line in reader.readlines():
            if line == '\n':
                customs.append(group)
                passenger_count.append(num_passengers)
                group = []
                num_passengers = 0
            else:
                num_passengers += 1

            for char in list(line.strip()):
                group.append(char)

        customs.append(group)
        passenger_count.append(num_passengers)



def part_1():
    count = 0
    for custom in customs:
        count += len(set(custom))

    return count

def part_2():
    count = 0
    for idx, custom in enumerate(customs):
        for char in set(custom):
            if custom.count(char) == passenger_count[idx]:
                count +=1
    return count

process_customs()
print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))