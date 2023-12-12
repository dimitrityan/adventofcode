def solve():
    cards = read_input("adventofcode/src/bin/day04/input.txt")
    points = 0
    for card in cards:
        winning_and_selected_nums = card.split(":")[1].strip().split("|")
        winning_nums = set(winning_and_selected_nums[0].strip().split(" "))
        selected_nums = set(winning_and_selected_nums[1].strip().split(" "))
        selected_nums = set(filter(lambda x: x != '', selected_nums))
        winning_nums = set(filter(lambda x: x != '', winning_nums))
        matches = len(selected_nums.intersection(winning_nums))
        points += 0 if matches == 0 else 2**(matches-1)
    print(points)


def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()