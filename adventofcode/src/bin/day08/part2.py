import math

def solve():
    lines = read_input("adventofcode/src/bin/day08/input.txt")
    directions = lines[0]
    lines = lines[2:]

    graph = {}
    start_nodes = []
    for line in lines:
        node = line.split(" = ")[0]
        left_right_raw = line.split(" = ")[1].split(", ")
        left = left_right_raw[0][1:]
        right = left_right_raw[1][:-1]
        graph[node] = (left, right)
        if node[-1] == 'A':
            start_nodes.append(node)
    
    i = 0
    count = 0
    target = "Z"
    end_nodes_and_steps = {}

    for node in start_nodes:
        i = 0
        count = 0
        start_node = node
        current_node = node
        seen = []
        while True:
            if i >= len(directions):
                i = 0
            direction = directions[i]
            count += 1
            if direction == "R":
                current_node = graph[current_node][1]
            elif direction == "L":
                current_node = graph[current_node][0]
            if current_node in seen:
                break
            if current_node[-1] == target:
                seen.append(current_node)
                end_nodes_and_steps[start_node] = count
            i += 1
    lcm = math.lcm(*list(end_nodes_and_steps.values()))
    print(lcm)
        
def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()