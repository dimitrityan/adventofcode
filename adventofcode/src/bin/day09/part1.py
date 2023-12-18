def solve():
    lines = read_input("adventofcode/src/bin/day09/input.txt")

    sum = 0
    for sequence in lines:
        sum += get_next_value([int(x) for x in sequence.split(" ")])
    
    print(sum)

def get_next_value(sequence):
    generated_sequences = [sequence]

    all_zeroes = False
    while not all_zeroes:
        generated_sequence = []
        for i in range(0, len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            generated_sequence.append(diff)
        if not any(generated_sequence):
            all_zeroes = True
        generated_sequences.append(generated_sequence)
        sequence = generated_sequence
    for i in range(len(generated_sequences) - 2, -1, -1):
        seq = generated_sequences[i]
        seq.append(generated_sequences[i + 1][-1] + seq[-1])
    
    return generated_sequences[0][-1]

        
def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def main():
    """ Main program """
    solve()

if __name__ == "__main__":
    main()