def solve():
    grid = read_input("adventofcode/src/bin/day10/example.txt")

    start_node = None
    for r in grid:
        r.insert(0, ".")
        r.append(".")
        for c in grid[r]:
            if grid[r][c] == "S":
                start_node = (r, c)
    grid.insert(0, ["."] * len(grid[0]))
    grid.append(["."] * len(grid[0]))
    
    queue = [(start_node, 0)]
    while len(queue) > 0:
        node_dist = queue.pop(0)
        node = node_dist[0]
        row = node[0]
        col = node[1]

        dist = node_dist[1]

    print(sum)

def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()