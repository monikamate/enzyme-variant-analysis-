def read_msa_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def Calculate_amino_acid_usage(msa_lines):
    amino_acid_usage = []

    #extract amino acid sequences for each sequence in the msa
    sequences = [line.split()[-1] for line in msa_lines if line.strip() and not line.startswith(' ')]

    # calculate amino acid usage at each position
    max_length = max(map(len, sequences))

    for position in range(max_length):
        amino_acids_at_position = [seq[position] if position < len(seq) else '-' for seq in sequences]
        amino_acid_count = {aa: amino_acids_at_position.count(aa) for aa in set(amino_acids_at_position)}
        amino_acid_usage.append(amino_acid_count)

    return amino_acid_usage

def print_amino_acid_usage(amino_acid_usage):
    for position, counts in enumerate(amino_acid_usage, start=1):
        print(f"Position {position}:")

        for amino_acid, count in counts.items():
            print(f"  {amino_acid}: {count}")

if __name__ == "__main__":
    msa_file_path = 'msa results.txt'

    #read the msa file
    msa_lines = read_msa_file(msa_file_path)

    # calculate amino acid usage
    amino_acid_usage = Calculate_amino_acid_usage(msa_lines)

    # print amino acid usage for each position
    print_amino_acid_usage(amino_acid_usage)                    