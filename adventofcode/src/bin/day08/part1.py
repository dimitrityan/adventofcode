def solve():
    lines = read_input("adventofcode/src/bin/day08/input.txt")
    directions = lines[0]
    lines = lines[2:]

    graph = {}
    for line in lines:
        node = line.split(" = ")[0]
        left_right_raw = line.split(" = ")[1].split(", ")
        left = left_right_raw[0][1:]
        right = left_right_raw[1][:-1]
        graph[node] = (left, right)
    
    i = 0
    count = 0
    current_node = "AAA"
    target = "ZZZ"
    while True:
        if i >= len(directions):
            i = 0
        direction = directions[i]
        count += 1
        if direction == "R":
            current_node = graph[current_node][1]
        elif direction == "L":
            current_node = graph[current_node][0]
        if current_node == target:
            break
        i += 1
    print(count)

        
def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()