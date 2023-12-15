# Multiple Sequence Alignment (MSA) Analysis

## Reading MSA File

Reading a multiple sequence alignment (MSA) file and returning its content as a list of lines.

### Parameters:
- `file_path` (str): Path to the MSA file.

### Returns:
- `msa_lines` (list): List of lines from the MSA file.

### Usage:
```python
def read_msa_file(file_path):

    Read content from a multiple sequence alignment (MSA) file.

    Args:
        file_path (str): Path to the MSA file.

    Returns:
        list: List of lines from the MSA file.
```
## Calculating Amino Acid Usage
Calculating amino acid usage for each position in the MSA.

### Parameters:
- `msa_lines` (list): List of lines from the MSA file.
### Returns:
- `amino_acid_usage` (list): List of dictionaries representing amino acid counts at each position.
### Usage:
```python
def Calculate_amino_acid_usage(msa_lines):

    Calculate amino acid usage for each position in the MSA.

    Args:
        msa_lines (list): List of lines from the MSA file.

    Returns:
        list: List of dictionaries representing amino acid counts at each position.

```
## Printing Amino Acid Usage
Printing amino acid usage for each position in the MSA.

### Parameters:
- `amino_acid_usage` (list): List of dictionaries representing amino acid counts at each position.
### Usage:
```python
def print_amino_acid_usage(amino_acid_usage):

    Print amino acid usage for each position in the MSA.

    Args:
        amino_acid_usage (list): List of dictionaries representing amino acid counts at each position.

    Returns:
        None
```
## Main Section
Handling the execution of the script.

### Usage:
```python
if __name__ == "__main__":
    msa_file_path = 'msa results.txt'

    #read the msa file
    msa_lines = read_msa_file(msa_file_path)

    # calculate amino acid usage
    amino_acid_usage = Calculate_amino_acid_usage(msa_lines)

    # print amino acid usage for each position
    print_amino_acid_usage(amino_acid_usage)
```
