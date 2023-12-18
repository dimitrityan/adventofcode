def solve():
    grid = read_input("adventofcode/src/bin/day10/input.txt")
    grid = [list(x) for x in grid]

    for r in range(0, len(grid)):
        grid[r].insert(0, ".")
        grid[r].append(".")
    grid.insert(0, ["."] * len(grid[0]))
    grid.append(["."] * len(grid[0]))

    start_node = None
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] == "S":
                start_node = (r, c)
    
    replace_start(grid, start_node[0], start_node[1])

    queue = [(start_node, 0)]
    longest_dist = -1
    seen = []
    while len(queue) > 0:
        node_dist = queue.pop(0)
        node_coords = node_dist[0]
        row = node_coords[0]
        col = node_coords[1]
        seen.append((row, col))
        node = grid[row][col]
        dist = node_dist[1]

        if dist > longest_dist:
            longest_dist = dist

        top_coord = (row-1, col)
        right_coord = (row, col+1)
        bottom_coord = (row+1, col)
        left_coord = (row, col-1)

        top = grid[top_coord[0]][top_coord[1]]
        right = grid[right_coord[0]][right_coord[1]]
        bottom = grid[bottom_coord[0]][bottom_coord[1]]
        left = grid[left_coord[0]][left_coord[1]]

        new_dist = dist + 1

        if is_top_bottom_compatible(top, node) and top_coord not in seen:
            queue.append((top_coord, new_dist))
        if is_top_bottom_compatible(node, bottom) and bottom_coord not in seen:
            queue.append((bottom_coord, new_dist))
        if is_left_right_compatible(left, node) and left_coord not in seen:
            queue.append((left_coord, new_dist))
        if is_left_right_compatible(node, right) and right_coord not in seen:
            queue.append((right_coord, new_dist))

    print(longest_dist)

def replace_start(grid, start_row, start_col):
    for i in ["|", "-", "L", "J", "7", "F"]:
        top = grid[start_row - 1][start_col]
        right = grid[start_row][start_col + 1]
        bottom = grid[start_row + 1][start_col]
        left = grid[start_row][start_col - 1]

        connecting = 0

        if is_top_bottom_compatible(top, i):
            connecting += 1
        if is_top_bottom_compatible(i, bottom):
            connecting += 1
        if is_left_right_compatible(left, i):
            connecting += 1
        if is_left_right_compatible(i, right):
            connecting += 1
        if connecting == 2:
            grid[start_row][start_col] = i
            break

def is_top_bottom_compatible(top, bottom):
    return bottom in ["|", "L", "J"] and top in ["7", "F", "|"]

def is_left_right_compatible(left, right):
    return left in ["-", "L", "F"] and right in ["-", "J", "7"]

def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()