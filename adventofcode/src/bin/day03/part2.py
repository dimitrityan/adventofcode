import re
from functools import reduce

def solve():
    grid = read_input("adventofcode/src/bin/day03/input.txt")
    potential_gear_to_count = {}

    for i in range(0, len(grid)):
        line = grid[i]
        numbers = re.compile(r'\d+').finditer(line)
        for number in numbers:
            for coord in get_gear_symbol_coords(grid, i, number.start(), number.end()-1):
                if coord not in potential_gear_to_count:
                    potential_gear_to_count[coord] = []
                potential_gear_to_count[coord].append(int(number.group()))
    gears_to_nums = dict(filter(lambda item: len(item[1]) == 2 , potential_gear_to_count.items()))
    res = reduce(lambda x, key:  x + (gears_to_nums[key][0] * gears_to_nums[key][1]), gears_to_nums, 0)

    print(res)

def get_gear_symbol_coords(grid, row, start_idx, end_idx):
    row_max = len(grid)
    gear_coords = []
    for i in range(max(row-1, 0), min(row+2, row_max)):
        col_max = len(grid[i])
        for j in range(max(start_idx-1, 0), min(end_idx+2, col_max)):
            if grid[i][j] == '*':
                gear_coords.append((i, j))
    return gear_coords

def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()