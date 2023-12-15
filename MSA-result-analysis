# Python Code in Markdown (.md) Format

```python
def read_msa_file(file_path):
    # Open and read the contents of the specified file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_amino_acid_usage(msa_lines):
    # Initialize an empty list to store amino acid usage at each position
    amino_acid_usage = []

    # Extract amino acid sequences for each sequence in the MSA
    sequences = [line.split()[-1] for line in msa_lines if line.strip() and not line.startswith(' ')]

    # Calculate amino acid usage at each position
    max_length = max(map(len, sequences))

    for position in range(max_length):
        amino_acids_at_position = [seq[position] if position < len(seq) else '-' for seq in sequences]
        amino_acid_count = {aa: amino_acids_at_position.count(aa) for aa in set(amino_acids_at_position)}
        amino_acid_usage.append(amino_acid_count)

    return amino_acid_usage

def print_amino_acid_usage(amino_acid_usage):
    # Print amino acid usage for each position
    for position, counts in enumerate(amino_acid_usage, start=1):
        print(f"Position {position}:")

        for amino_acid, count in counts.items():
            print(f"  {amino_acid}: {count}")

if __name__ == "__main__":
    # Set the path to the MSA file
    msa_file_path = 'msa results.txt'

    # Read the MSA file
    msa_lines = read_msa_file(msa_file_path)

    # Calculate amino acid usage
    amino_acid_usage = calculate_amino_acid_usage(msa_lines)

    # Print amino acid usage for each position
    print_amino_acid_usage(amino_acid_usage)
