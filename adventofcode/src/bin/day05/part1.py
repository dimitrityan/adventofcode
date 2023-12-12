def solve():
    input = read_input("adventofcode/src/bin/day05/input.txt")
    seeds = list(map(lambda x: int(x), input[0].split(":")[1].strip().split(" ")))

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
    for seed in seeds:
        src = seed
        for mappings in maps_int:
            src = get_destination(src, mappings)
        if src < closest_location:
            closest_location = src
    print(closest_location)

def get_destination(source, mappings):
    for mapping in mappings:
        map_dst = mapping[0]
        map_src = mapping[1]
        map_stp = mapping[2]
        if map_src <= source and source <= map_src + map_stp - 1:
            return map_dst + source - map_src
    return source


def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()