import re
import time

SEEDS = []

'''
e.g.
seed-to-soil map:
50 98 2
52 50 48

# Map [
    {'diff': -48, 'source-low': 98, 'source-high': 99, 'destination-low': 50, 'destination-high': 51},
    {'diff': 2, 'source-low': 50, 'source-high': 97, 'destination-low': 52, 'destination-high': 99},
]
'''
SEED_TO_SOIL = []
SOIL_TO_FERT = []
FERT_TO_WATER = []
WATER_TO_LIGHT = []
LIGHT_TO_TEMP = []
TEMP_TO_HUMIDITY = []
HUMIDITY_TO_LOCATION = []


def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            if 'seeds:' in line:
                SEEDS.extend(re.findall(r'\d+', line))
            elif 'seed-to-soil map:' in line:
                CUR_ARRAY = SEED_TO_SOIL
            elif 'soil-to-fertilizer map:' in line:
                CUR_ARRAY = SOIL_TO_FERT
            elif 'fertilizer-to-water map:' in line:
                CUR_ARRAY = FERT_TO_WATER
            elif 'water-to-light map:' in line:
                CUR_ARRAY = WATER_TO_LIGHT
            elif 'light-to-temperature map:' in line:
                CUR_ARRAY = LIGHT_TO_TEMP
            elif 'temperature-to-humidity map:' in line:
                CUR_ARRAY = TEMP_TO_HUMIDITY
            elif 'humidity-to-location map:' in line:
                CUR_ARRAY = HUMIDITY_TO_LOCATION
            elif line[0].isdigit():
                data = line.replace('\n', '').split(' ')
                source = int(data[1])
                destination = int(data[0])
                length = int(data[2])
                CUR_ARRAY.append(
                    {
                        'diff': destination - source,
                        'source-low': source,
                        'source-high': source + length - 1,
                        'destination-low': destination,
                        'destination-high': destination + length - 1,
                    },
                )

def get_map_value(source, MAP):
    source = int(source)
    for line in MAP:
        if source >= line['source-low'] and source <= line['source-high']:
            return source + line['diff']

    return source


def process_seeds(SEEDS):
    MODIFIED_SEEDS = []
    skip_next = False
    for index, seed in enumerate(SEEDS):
        if skip_next == True:
            skip_next = False
            continue

        skip_next = True  
        seed = int(seed)      

        MODIFIED_SEEDS.extend(range(seed, seed+int(SEEDS[index+1])))

    return MODIFIED_SEEDS

def part_1():
    min_location = -1
    for seed in SEEDS:
        soil = get_map_value(seed, SEED_TO_SOIL)
        fert = get_map_value(soil, SOIL_TO_FERT)
        water = get_map_value(fert, FERT_TO_WATER)
        light = get_map_value(water, WATER_TO_LIGHT)
        temp = get_map_value(light, LIGHT_TO_TEMP)
        humidity = get_map_value(temp, TEMP_TO_HUMIDITY)
        location = get_map_value(humidity, HUMIDITY_TO_LOCATION)
        if min_location == -1 or location <= min_location:
            min_location = location

    return min_location

def part_2():
    start = time.time()
    MODIFIED_SEEDS = process_seeds(SEEDS)
    end = time.time()
    print(end - start)
    min_location = -1
    start = time.time()
    for seed in MODIFIED_SEEDS:
        soil = get_map_value(seed, SEED_TO_SOIL)
        fert = get_map_value(soil, SOIL_TO_FERT)
        water = get_map_value(fert, FERT_TO_WATER)
        light = get_map_value(water, WATER_TO_LIGHT)
        temp = get_map_value(light, LIGHT_TO_TEMP)
        humidity = get_map_value(temp, TEMP_TO_HUMIDITY)
        location = get_map_value(humidity, HUMIDITY_TO_LOCATION)
        if min_location == -1 or location <= min_location:
            min_location = location
    end = time.time()
    print(end - start)
    

    return min_location


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")
