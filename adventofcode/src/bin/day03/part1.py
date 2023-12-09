import re

def solve():
    grid = read_input("adventofcode/src/bin/day03/example.txt")
    res = 0
    for i in range(0, len(grid)):
        line = grid[i]
        numbers = re.compile(r'\d+').finditer(line)
        for number in numbers:
            if (has_adjacent_symbol(grid, i, number.start(), number.end()-1)):
                res += int(number.group())
    print(res)

def has_adjacent_symbol(grid, row, start_idx, end_idx):
    row_max = len(grid)
    for i in range(max(row-1, 0), min(row+2, row_max)):
        col_max = len(grid[i])
        for j in range(max(start_idx-1, 0), min(end_idx+2, col_max)):
            if is_symbol(grid[i][j]):
                return True
    return False

def is_symbol(c):
    return c != '.' and not c.isdigit()

def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()