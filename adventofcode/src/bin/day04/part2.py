from functools import reduce

def solve():
    cards = read_input("adventofcode/src/bin/day04/input.txt")
    card_copies = {}
    card_copies[0] = 1
    for i, card in enumerate(cards):
        copies = card_copies.setdefault(i, 1)
        winning_and_selected_nums = card.split(":")[1].strip().split("|")
        winning_nums = set(winning_and_selected_nums[0].strip().split(" "))
        selected_nums = set(winning_and_selected_nums[1].strip().split(" "))
        selected_nums = set(filter(lambda x: x != '', selected_nums))
        winning_nums = set(filter(lambda x: x != '', winning_nums))
        num_wins = len(selected_nums.intersection(winning_nums))
        for j in range(1, num_wins + 1):
            winning_copy = i + j
            card_copies.setdefault(winning_copy, 1)
            card_copies[winning_copy] += copies

    res = reduce(lambda x, key: x + card_copies[key], card_copies, 0)
    print(card_copies)
    print(res)

def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()