def solve():
    input = read_input("adventofcode/src/bin/day05/input.txt")
    seeds = list(map(lambda x: int(x), input[0].split(":")[1].strip().split(" ")))
    seeds = list(zip(seeds[::2], seeds[1::2]))

    input_split = []
    tmp = []
    for i in range(2, len(input)):
        if input[i] == "":
            input_split.append(tmp)
            tmp = []
        else:
            tmp.append(input[i])
        if i == len(input) - 1:
            input_split.append(tmp)
    
    maps_int = []
    for input_split_val in input_split:
        maps_int.append(list(map(lambda x: list(map(lambda v: int(v), x.split(" "))), input_split_val[1:])))
    
    closest_location = float('inf')
    for seed, step in seeds:
        seed_range = (seed, seed + step - 1)
        for mappings in maps_int:
            src = get_destination(seed_range, mappings)
        if src < closest_location:
            closest_location = src
    print(closest_location)

def get_destination(seed_range, mappings):
    unmapped_ranges = [seed_range]
    mapped_ranges = []
    for seed_start, seed_end in unmapped_ranges:
        for mapping in mappings:
            map_dst = mapping[0]
            map_src = mapping[1]
            map_stp = mapping[2]
            map_range_start = map_src
            map_range_end = map_src + map_stp - 1
            if map_range_start <= seed_start and seed_end <= map_range_end:
                # if fully inside mapped range, apply transformation to start and end
                seed_size = seed_end - seed_start
                new_mapped_start = map_dst + seed_start - map_range_start
                new_mapped_end = map_dst + seed_start - map_range_start + seed_size
                mapped_ranges.append((new_mapped_start, new_mapped_end))
            elif seed_start < map_range_start and seed_end >= map_range_start and seed_end <= map_range_end:
                unmapped_ranges.append((seed_start, map_range_start - seed_start))
                new_mappend_end = seed_end - map_range_start
                mapped_ranges.append((map_dst, map_dst + new_mapped_end))
            elif (seed_start < map_range_start and seed_end < map_range_start) or (seed_start > map_range_end and seed_end > map_range_end):
                

    return source


def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()