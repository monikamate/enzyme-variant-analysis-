# PDB to CSV Converter and Loop Analyzer

The provided Python script utilizes the Biopython library to convert a PDB (Protein Data Bank) file to a CSV (Comma-Separated Values) file and analyzes loops in the protein structure.

## PDB to CSV Conversion Function

The script defines a function `pdb_to_csv` that converts PDB file data into a CSV format. It extracts information such as atom details, residue names, chain identifiers, and coordinates, writing this information to a specified CSV file.

```python
from Bio import PDB
import csv

def pdb_to_csv(pdb_file, csv_file):
    # PDB parser object
    structure = PDB.PDBParser(QUIET=True).get_structure('structure', pdb_file)

    # Write CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(['Record', 'Atom', 'Residue', 'Chain', 'X', 'Y', 'Z', 'B-Factor'])

        # Write data
        for model in structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        row = [
                            atom.get_full_id()[0],  # Record type (ATOM or HETATM)
                            atom.get_name(),        # Atom name
                            residue.get_resname(),   # Residue name
                            chain.get_id(),          # Chain identifier
                            *atom.get_coord(),       # X, Y, Z coordinates
                            atom.get_bfactor()       # B-factor
                        ]
                        csv_writer.writerow(row)
