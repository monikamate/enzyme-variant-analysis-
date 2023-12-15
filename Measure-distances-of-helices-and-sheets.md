# Measure Distances of helices and sheets

The provided Python code is a script that utilizes the Biopython library to analyze the structure of a protein in a PDB (Protein Data Bank) file. The primary purpose of the script is to identify potential helix structures within a specified distance threshold.

## PDB Structure Distance Calculation

### Importing Modules and Suppressing Warnings

Importing necessary modules and suppressing warnings for cleaner output.

### Usage:
```python
import warnings
from Bio.PDB import PDBParser

warnings.filterwarnings("ignore")
```
### PDB Parser and Structure Reading
Parsing a PDB file and reading the structure from the file.

### Usage:
```python
parser = PDBParser()

pdb_file = r"~\8TIM.pdb"

structure = parser.get_structure('8TIM', pdb_file)

model = structure[0]
chain = model['A']
```
### Helix Distance Calculation
Calculating the distance between alpha carbon (CA) atoms in a single chain.

### Usage:
```python
for residue1 in chain:
    for residue2 in chain:
        if residue1 != residue2:
            try:
                distance = residue1['CA'] - residue2['CA']
            except KeyError:
                continue
            if distance < 6:
                print(
                    f"Helix ID: ({residue1.get_id()}, {residue2.get_id()}), Distance: {distance:.3f} \u00C5"
                )
        break
```
