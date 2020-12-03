def process_tree(col, row):
    with open('input.txt') as reader:
        row_count = 0
        col_count = 0
        tree_count = 0
        for line in reader.readlines():
            line = list(line.strip('\n'))
            if row_count % row == 0:
                if line[col_count % len(line)] == '#':
                    tree_count += 1
                col_count += col
            
            row_count += 1
    return tree_count 

def part_1():
    return process_tree(3,1)

def part_2():
    return (
        process_tree(1,1) *
        process_tree(3,1) *
        process_tree(5,1) *
        process_tree(7,1) *
        process_tree(1,2)
    )


print("Answer for part 1: {}".format(part_1()))
print("Answer for part 2: {}".format(part_2()))