def solve():
    lines = read_input("adventofcode/src/bin/day07/input.txt")
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    cards_bids = []

    for line in lines:
        line = line.split(" ")
        cards = line[0]
        bid = line[1]
        cards_bid = (cards, bid)
        
        cards_dict = {}
        for card in cards:
            cards_dict[card] = cards_dict.get(card, 0) + 1
            cards_bids.append(cards_bid)

        sorted_cards = list(reversed(sorted(cards_dict.items(), key=lambda x:x[1])))
        most_common_card = sorted_cards[0][1]
        num_diff_cards = len(cards_dict.keys())
        if most_common_card == 5:
            five_of_a_kind.append(cards_bid)
        elif num_diff_cards == 2 and most_common_card == 4:
            four_of_a_kind.append(cards_bid)      
        elif num_diff_cards == 2 and most_common_card == 3:
            full_house.append(cards_bid)
        elif num_diff_cards == 3 and most_common_card == 3:
            three_of_a_kind.append(cards_bid)
        elif num_diff_cards == 3 and most_common_card == 2:
            two_pair.append(cards_bid)
        elif num_diff_cards == 4 and most_common_card == 2:
            one_pair.append(cards_bid)
        elif most_common_card == 1:
            high_card.append(cards_bid)

    ranked_bets = []
    alphabet = "23456789TJQKA"
    
    ranked_bets += sorted(high_card, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(one_pair, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(two_pair, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(three_of_a_kind, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(full_house, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(four_of_a_kind, key=lambda x: [alphabet.index(c) for c in x[0]])
    ranked_bets += sorted(five_of_a_kind, key=lambda x: [alphabet.index(c) for c in x[0]])

    sum = 0
    for i in range(0, len(ranked_bets)):
        sum += int(ranked_bets[i][1]) * (i + 1)
    
    print(sum)
        
def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()